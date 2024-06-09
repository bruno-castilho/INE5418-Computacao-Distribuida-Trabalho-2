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
docker build -t app_tuple_space:latest .


docker run -it --network=zookeeper-ensemble_default -e SERVES=zoo1:2181,zoo2:2181,zoo3:2181 app_tuple_space:latest


## Guia de Uso

## Tuplas Válidas