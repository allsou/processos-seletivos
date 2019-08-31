# GYPZ - Tech Challenge
Aplicação que permitirá a solicitação de um cartão de crédito, onde o usuário irá inserir suas informações básicas e o sistema irá fazer uma análise da liberação do cartão.

## BackEnd - RESTful API
API capaz de interpretar os seguintes verbos em suas respectivas URIs:

| Método    | URI                           | Ação                                      |
| --------- | ----------------------------- | ----------------------------------------- |
| GET       | http://{host}/cardrequest     | Traz todas solicitações existentes        |
| POST      | http://{host}/cardrequest     | Cria nova solicitação                     |
| DELETE    | http://{host}cardrequest/{id} | Exclui a solicitação {id}                 |

### Bibliotecas Utilizadas
* [Flask] (https://palletsprojects.com/p/flask/) - Microframework
* [Flask-RESTful] (https://flask-restful.readthedocs.io/en/latest/) - Suporte a recursos
* [Flask-CORS] (https://flask-cors.readthedocs.io/en/latest/) - Cross Origin Resource Sharing

## FrontEnd
UIs desenvolvidas para realizar a interação com a API.

### Bibliotecas
* [React] (https://reactjs.org/) - Biblioteca JS
* [axios] (https://github.com/axios/axios) - Cliente HTTP
* [Primitive CSS] (https://taniarascia.github.io/primitive/) - Estilos minimalistas

