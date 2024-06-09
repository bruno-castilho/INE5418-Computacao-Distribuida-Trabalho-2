from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.exceptions import *
import os

serves = os.getenv('SERVES')

class TupleSpace:
    def sync_tuples(self, childrens):
        current_tuples = set(childrens)
        old_tuples = set(self.tuples.keys())

        tuples_to_be_rm = old_tuples - current_tuples
        tuples_to_be_add = current_tuples - old_tuples


        for znode in tuples_to_be_add:
            self.tuples[znode] = eval(self.zk.get(f'/tuples/{znode}')[0].decode('utf-8'))

        for znode in tuples_to_be_rm:
            del self.tuples[znode]

    def status_listener(self, state): 
        if state == KazooState.LOST:
            self.STATE = 'LOST'
        elif state == KazooState.SUSPENDED:
            self.STATE = 'SUSPENDED'
        else:
            self.STATE = 'CONNECTED'

    def __init__(self):
        self.tuples = {}
        self.STARTING = True
        self.STATE = 'LOST'

        self.zk = KazooClient(hosts=serves)
        self.zk.add_listener(self.status_listener)
        self.zk.start()



        if(not self.zk.exists("/tuples")):
            self.zk.ensure_path("/tuples")


        self.zk.ChildrenWatch('/tuples', func=self.sync_tuples)

    def write(self, p):
        try:
            self.zk.create('/tuples/tuple_', value=str(p).encode('utf-8'), sequence=True, include_data=True)
            return True
        except:
            return False

    def read(self, p):
        for znode in self.tuples:
            if(len(self.tuples[znode]) == len(p)):
                is_the_tuple = True
                for i in range(len(p)):
                    if(p[i] != '*' and self.tuples[znode][i] != p[i]):
                        is_the_tuple = False
                        break
                
                if(is_the_tuple): return self.tuples[znode]

        
        return ()
    
    def get(self, p):
        while(self.STATE == 'CONNECTED'):
            for znode in self.tuples:
                if(len(self.tuples[znode]) == len(p)):
                    is_the_tuple = True
                    for i in range(len(p)):
                        if(p[i] != '*' and self.tuples[znode][i] != p[i]):
                            is_the_tuple = False
                            break
                    
                    if(is_the_tuple):         
                        try: 
                            tuple = self.tuples[znode]
                            self.zk.delete(f"/tuples/{znode}")
                            return tuple
            
                        except NoNodeError:
                            pass
                        
    def end(self):
        self.zk.stop()

    def getState(self):
        return self.STATE

    def debug(self):
        print('************************************************************')
        print(self.tuples)
