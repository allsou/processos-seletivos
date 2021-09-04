# Approved?
![](https://github.com/allsou/ProcessosSeletivos/blob/master/assets/check-mark.png)

# Favorites
Service responsible to manage favorite products.

## Prerequisites
These must be installed to run the application.
* [makefile](https://makefiletutorial.com/)
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Build
To build the project, you will need to type `make build`, after this you can run anothers commands on the project.
This will download docker images such as python and mongo.
> $ make build
```python
...
Step 9/9 : ENTRYPOINT python server.py
 ---> Running in e86cc9cf2dab
Removing intermediate container e86cc9cf2dab
 ---> 52006d98d11c
Successfully built 52006d98d11c
Successfully tagged luizalabs_favorites:latest
```

## Up services
Will start services or update.
> $ make up
```python
...
luizalabs_favorites_1 is up-to-date
luizalabs_mongo_1 is up-to-date
```

## Watch logs
To see logs registered at console.
> $ make watch
```python
...
favorites_1  | settings.py [initialize] #[29] - DEBUG - Initiate setup
favorites_1  | settings.py [connect_to_mongo_database] #[22] - INFO - Connecting to mongo...
favorites_1  | settings.py [connect_to_mongo_database] #[24] - INFO - Mongo connected!
favorites_1  | server.py [main] #[15] - INFO - Favorites Service at 0.0.0.0 listening 3001
```

## Shortcut
Build, up and watch services.
> $ make build up watch

## API Usage
A OAuth are implemented, so its necessery send a Bearer Token to requests.
### Getting token
The provider setup to check authentication is [Auth0](https://auth0.com/) and to get the token are necessary to make a request with credentials from e-mail sent.
```pycon
curl --request POST \
  --url https://dev-zecijt20.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"","client_secret":"","audience":"http://localhost:3000","grant_type":"client_credentials"}'
```
Response
```pycon
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6I...",
  "token_type": "Bearer"
}
```
### Requesting API
After token obtained, the requests can be done using the token and payload specified at requests collections
```python
curl --location --request POST 'http://localhost:3001/api/product' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtp...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "price": 2199.99,
    "image": "https://a-static.mlcdn.com.br/618x463/smartphone-samsung-galaxy-s20-fe-128gb-cloud-navy-4g-6gb-ram-tela-65-cam-tripla-selfie-32mp/magazineluiza/155629800/0007bbdc665749ec107d860c3a4b8b2f.jpg",
    "brand": "Samsung",
    "title": "Smartphone Samsung Galaxy S20 FE 128GB Cloud Navy - 4G 6GB RAM Tela 6,5” Câm. Tripla + Selfie 32MP",
    "reviewScore": 4.35
}'
```
### Request Collections
If necessary, all requests are already setup at a [Postman](https://www.postman.com/) collection in docs directory
- [./docs/Magalu.postman_collection.json](https://github.com/allsou/luizalabs/blob/develop/docs/Magalu.postman_collection.json)

## Tests
In this option you will run only lint and unit tests.
> $ make test-unit

# Made using
- [Mongoengine](http://mongoengine.org/) - ORM  
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Dependencies manager
- [Pytest](https://docs.pytest.org/en/latest) - Test Framework  
- [python-jose](https://github.com/mpdavis/python-jose) - JWT
- [Starlette](https://www.starlette.io) - Framework/Toolkit
- [Uvicorn](https://www.uvicorn.org) - ASGI server
