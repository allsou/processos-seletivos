# Approved?
![](https://github.com/allsou/ProcessosSeletivos/blob/master/assets/check-mark.png)

# Dock
Serviço para criação de contas digitais.

## Pré-requisitos
Os seguintes softwares precisam ser instalados para poder utilizar esta aplicação:
* [makefile](https://makefiletutorial.com/)
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Organização
### Componentes
Organização dos componentes conforme implementado.
![](https://github.com/allsou/dock-dev-api-rest-test/blob/feature/dock/docs/assets/components.png)

### Entidades
Entidades referência para persistencia de dados e validações.
![](https://github.com/allsou/dock-dev-api-rest-test/blob/feature/dock/docs/assets/entities.png)

## Deploy
### Build
Para realizar o build do projeto, será necessário executar o comando `make build`, após isso será possível executar os demais commandos do projeto.
Isso irá realizar o download das imagens docker e criar os containers como o da aplicação, mongo e redis.
**ATENÇÃO**: As variáveis de ambiente precisam estar configuradas em arquivo `.env`, existe um exemplo no repositório como [.env_template](https://github.com/allsou/dock-dev-api-rest-test/blob/feature/dock/.env_template) basta renomea-lo para `.env` antes de iniciar o comando.
> $ make build
```python
...
Step 7/7 : ENTRYPOINT python server.py
 ---> Running in 31d0ae456d38
Removing intermediate container 31d0ae456d38
 ---> b8410cc36f27

Successfully built b8410cc36f27
Successfully tagged dock-dev-api-rest-test_dock:latest
```

### Serviços
O seguinte comando irá iniciar os serviços ou realizar atualização.
> $ make up
```python
...
Creating network "dock-dev-api-rest-test_dock-net" with the default driver
Creating dock-dev-api-rest-test_redis_1 ... done
Creating dock-dev-api-rest-test_dock_1  ... done
Creating dock-dev-api-rest-test_mongo_1 ... done
```

### Verificar logs
Para verificar os logs no console.
> $ make watch
```python
...
dock_1   | base.py [initialize] #[39] - DEBUG - Start setup
dock_1   | base.py [connect_to_mongo_database] #[25] - INFO - Connecting to mongo...
dock_1   | base.py [connect_to_mongo_database] #[27] - INFO - Mongo connected!
dock_1   | base.py [create_redis_pool] #[31] - INFO - Opening redis pool...
dock_1   | base.py [create_redis_pool] #[34] - INFO - Redis pool opened!
dock_1   | server.py [cli_run] #[24] - INFO - Dock Service on 0.0.0.0 port 8001
```

### Testes
Este comando irá executar os testes unitários.

> $ make test-unit
---
**Não tive tempo disponível para conseguir realizar uma cobertura ideal, os testes aqui são apenas alguns exemplos de como faço ^^**

## Utilização da API
Segue algumas informações para a utilização da API.
### Requisições
Se necessário, todas as requisições já estão configuradas em uma coleção do [Postman](https://www.postman.com/) no diretório [docs](https://github.com/allsou/dock-dev-api-rest-test/tree/feature/dock/docs).
- [./docs/Dock.postman_collection.json](https://github.com/allsou/dock-dev-api-rest-test/blob/feature/dock/docs/Dock.postman_collection.json)
Segue exemplo de requisição:
```pycon
curl --location --request POST 'http://localhost:80/api/v0/holders' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Igor Dinho",
    "tax_id": "300.081.300-43"
}'
```
Response
```pycon
{
    "message": [],
    "data": {
        "_id": "624251d30a08923b58a52599",
        "name": "IGOR DINHO",
        "tax_id": "30008130043"
    }
}
```
#### Endpoints
Os endpoints estão disponíveis em swagger no diretório [docs](https://github.com/allsou/dock-dev-api-rest-test/tree/feature/dock/docs) ou em `/docs` da API.
![](https://github.com/allsou/dock-dev-api-rest-test/blob/feature/dock/docs/assets/swagger.png)

## CI
Foi configurado um CI, via Github Actions para rodar lint e testes toda vez que for realizado um `push`.
- https://github.com/allsou/dock-dev-api-rest-test/actions

## Publicação
Não realizei a configuração de entrega continua, mas fiz a publicação manual desta API na AWS, o endereço do host é este: ec2-3-229-93-101.compute-1.amazonaws.com

---

**Esta aplicação ficará ligada apenas no horário das 09:00 ás 16:00 nos próximos 3 dias caso queiram realizar algum teste, isso visa a redução de custos =)**

## Feito usando
- [Flake8](https://flake8.pycqa.org/en/latest/) - Style Guide
- [Mongoengine](http://mongoengine.org/) - ORM  
- [Pytest](https://docs.pytest.org/en/latest) - Test Framework
- [Redis-py](https://github.com/redis/redis-py) - Redis Driver to cache  
- [Starlette](https://www.starlette.io) - Framework/Toolkit
- [Uvicorn](https://www.uvicorn.org) - ASGI server
* And other dependecies...