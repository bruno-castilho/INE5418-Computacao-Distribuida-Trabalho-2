# INE5418-Computacao-Distribuida-Trabalho-2
## Descrição

## Pre-Requesito
[Docker](https://docs.docker.com/engine/install/)

[Docker Compose](https://docs.docker.com/compose/install/)



## Inicializando Zookeeper Ensemble

Inicialize os containers utilizando o Docker Compose. Na pasta `zookeeper-ensemble` do projeto, execute o seguinte comando:
```bash
  docker compose up -d
```


## Inicializando Clientes

Compile a imagem do cliente. Na pasta app_tuple_space do projeto, execute o comando abaixo:
```bash
docker build -t app_tuple_space:latest .
```
Inicie um contêiner com o cliente na rede do Zookeeper Ensemble, que foi inicializado anteriormente. Para isso, execute o comando abaixo:
```bash
docker run -it --network=zookeeper-ensemble_default -e SERVES=zoo1:2181,zoo2:2181,zoo3:2181 app_tuple_space:latest
```
## Guia de Uso
Se tudo ocorrer bem no passo anterior, um menu com as opções do cliente deve aparecer durante a execução do contêiner. Ao escolher uma das opções, será solicitada uma tupla válida.

1 - Opção 0 busca uma tupla no sistema e a retorna ao usuário. Caso não a encontre, o sistema ficará travado até que uma tupla esteja disponível. Se encontrada, a tupla é removida do espaço de tuplas.

2 - Opção 1 insere uma tupla no espaço de tuplas.

3 - Opção 2 busca uma tupla no sistema e a retorna ao usuário. Caso não a encontre, retorna uma tupla vazia.

## Tuplas Válidas
Uma tupla válida é uma sequência ordenada de elementos (elemento1, ..., elementoN), onde elementos do tipo string são adicionados dentro de aspas ('').
Uma tupla de busca pode conter o caractere '*' como um elemento, onde aquela entrada da tupla pode ser qualquer coisa."

Exemplos de tuplas válidas:"
('INE540', 'Jorginho', 4, 3)\
('INE540', 'Jorginho')\
('INE540', 0)

Exemplos de tuplas de busca:
('INE540', 'Jorginho', 4, 3)\
('INE540', 0)\
('INE540', '\*', 4, 3)\
('INE540', '\*')
