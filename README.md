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

Compile a imagem do cliente. Na pasta `app_tuple_space` do projeto, execute o comando abaixo:
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
No contexto do cadastro de turmas em um espaço de tuplas distribuído, uma tupla válida segue um formato específico para garantir a consistência e a integridade dos dados. Cada tupla é composta por dois elementos:
Código da Turma: O primeiro elemento da tupla é uma string que representa o código da turma. Este código deve seguir o formato "AAA0000", onde:

"AAA" são três letras (maiúsculas ou minúsculas).

"0000" são quatro dígitos numéricos.

Número de Alunos: O segundo elemento da tupla é um número inteiro que representa o número de alunos na turma. Este número deve estar entre 1 e 100, inclusive.

## Exemplos de Tuplas Válidas
("CSC1010", 25): Representa uma turma de código "CSC1010" com 25 alunos.\
("MAT2022", 30): Representa uma turma de código "MAT2022" com 30 alunos.\
("ENG3030", 10): Representa uma turma de código "ENG3030" com 10 alunos.
