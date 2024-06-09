from TupleSpace import TupleSpace
from os import system, name
import time


tupleSpace = TupleSpace()

def clear(): 
    if name == 'nt': 
        system('cls') 

    else: 
        system('clear') 


def run():
        clear()
        print('O que você deseja fazer?')
        print('[0] Pegar uma tupla.')
        print('[1] Criar uma tupla.')
        print('[2] Ler uma tupla.')
        print('Ctrl + C para sair')
        
        picked = input("Digite a opção escolhida: ")

        if(picked == '0'):
            while(True):
                clear()
                try:
                    p = eval(input('Insira a tupla de referência: '))
                except:
                    print('Tupla inválida')
                    time.sleep(3)
                    continue
                print('Buscando tupla...')

                result = tupleSpace.get(p)
                if(result != None):
                    print('Tupla encontrada:', result)
                else:
                    print('Falha na conexão com o servidor')
                input('Pressione Enter para continuar')
                break
        elif(picked == '1'):
            while True: 
                clear()
                try:
                    p = eval(input('Insira a tupla: '))
                except:
                    print('Tupla inválida')
                    time.sleep(3)
                    continue

                print('Cadastrando tupla...')
                if tupleSpace.write(p):
                    print('Tupla cadastrada com sucesso')
                else:
                    print('Falha ao cadastrar tupla')

                input('Pressione Enter para continuar')
                break
        elif(picked == '2'):
            while True: 
                clear()
                try:
                    p = eval(input('Insira a tupla de referência: '))
                except:
                    print('Tupla inválida')
                    time.sleep(3)
                    continue
                print('Buscando tupla...')
                print('Tupla encontrada:', tupleSpace.read(p))
                input('Pressione Enter para continuar')
                break
        else: 
            clear()
            print('Opção não válida')
            input('Pressione Enter para continuar')


try:
    while(True):
        if(tupleSpace.getState() == 'CONNECTED'):
            run()
except:
    tupleSpace.end()

