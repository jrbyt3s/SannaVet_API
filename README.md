# SANNAVET



## Instalación y Activación d eentorno virtual:

1. install your enviroment: pipenv install
2. activate your enviroment: pipenv shell.

```sh
pipenv install Django
```

## Apuntes Django

- Crear un proyecto

```sh
django-admin startproject <nombre_proyecto> .
```

- Iniciar proyecto

```sh
python manage.py runserver
```

- Crear superusuario (Se ejecuta despues de las migraciones)

```sh
python manage.py createsuperuser
```

## Apps



- Crear una app

```sh
python manage.py startapp <nombre_app>
```

## Migraciones

- Sincronizar o Aplicar migraciones

```sh
python manage.py migrate
```

- Crear una migración

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

## Environment (.env)

```py
DEBUG=True

DEBUG=True

DB_NAME='drf_sannavet'
DB_USER='xxxxx'
DB_PASSWORD=''
DB_HOST='127.0.0.1'
DB_PORT='5432'

MAIL_SERVER=''
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=''
MAIL_PASSWORD=''

AWS_ACCESS_KEY_ID=''
AWS_ACCESS_KEY_SECRET=''
AWS_REGION=''

```
