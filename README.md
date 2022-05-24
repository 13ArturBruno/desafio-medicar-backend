# Medicar backend API
This repo contains a project api.

## Como rodar o projeto

steps:

Create a VirtualEnvironment

Install requirements:
```
$ pip install -r requirements.txt
```

Create a .env and set database configuration or set a default in settings.py

Run migrates in database:
```
$ python manager.py migrate
```

Create a superuser to access /admin:
```
$ python manager.py createsuperuser
```

Run application:
```
$ python manage.py runserver
```

# Trello configuration:

In .env, need add the following information:
```
TRELLO_API_KEY='*****'
TRELLO_API_TOKEN='*****'
TRELLO_LIST_ID='*****'
```