# DRF SannaVet API
![]()
![](https://raw.githubusercontent.com/jrbyt3s/sannavet/main/public/images/sannavet-logo-brand-removebg-resize.png)


## Instructions for local deploy

1. Clone the repository.
2. Open terminal and put follow command:

    ```sh
    pivenv install
    ```

3. You must set the Enriroment variables:
    ```py
    
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
4. You must activate virtual environment:
    ```sh
    pipenv shell
    ```

5. After that you need migrate in order to syncronize to DB:
    ```sh
    python manage.py migrate
    ```

6. After that you need:
    ```sh
    python manage.py migrate
    ```

7. Run the project and enjoy !
    ```sh
    python manage.py runserver
    ```



## DB Tables:

# Users


| Column Name        | constraint   | Data Type    |
|--------------------|--------------|--------------|
| user_id         | PRIMARY KEY  | SERIAL       |
| username            | NOT NULL     | VARCHAR(50)  |
| first_name            | NOT NULL     | VARCHAR(50)  |
| last_name          | NOT NULL     | VARCHAR(50)  |
| email              | NOT NULL     | VARCHAR(100) |
| password           | NOT NULL     | VARCHAR(100) |
| role               | NOT NULL	| (cliente, veterinario)|
| is_staff           | DEFAULT FALSE | BOOLEAN     |
| is_active          | DEFAULT TRUE | BOOLEAN      |
| ...                |              |


# Pets


| Column Name   | Constraint            | Data Type     |
|---------------|-----------------------|---------------|
| pet_id     | PRIMARY KEY           | SERIAL        |
| user_id     | FOREIGN KEY, NOT NULL | SERIAL        |
| Nombre        | NOT NULL              | VARCHAR(100)   |
| Sexo          | NOT NULL              | CHAR(1)       |
| Especie       | NOT NULL              | VARCHAR(50)   |
| Raza          | NOT NULL              | VARCHAR(50)   |
| Color         | NOT NULL              | VARCHAR(50)   |
| FotoUrl       | DEFAULT "example.com" | VARCHAR(200)   |
| Esterilizado  | NOT NULL              | BOOLEAN       |
| Peso          | DEFAULT 2.0           | DECIMAL(5,2)  |
| is_delete		| NOT NULL              | BOOLEAN       |




**Relaciones:**
- Mascota - Cita (1:N): Una mascota puede tener varias citas, pero cada cita pertenece a una única mascota.
- Mascota - Atenciones (1:N): Una mascota puede tener varias Atenciones, pero cada atencion pertenece a una única mascota.
- Mascota - CurrentAtentions (1:1): Cada mascota puede tener una atención actual en la veterinaria.


# Appoiment


| Column Name   | Constraint            | Data Type     |
|---------------|-----------------------|---------------|
| appoiment_id   | PRIMARY KEY           | SERIAL        |
| pet_id	     | FOREIGN KEY, NOT NULL | SERIAL        |
| veterinarian_id | FOREIGN KEY           | SERIAL        |
| date	      | NOT NULL              | DATE          |
| hour	      | NOT NULL              | TIME          |
| description 	|                       | TEXT          |
| payed  		| DEFAULT FALSE         | BOOLEAN       |
| state	      | DEFAULT FALSE         | BOOLEAN       |                      
| create_date   	| DEFAULT DATE_NOW      | DATE          |



# Attentions


| Column Name         | Constraint              | Data Type     |
|-------------------- |-------------------------|---------------|
| atencion_id  | PRIMARY KEY             | SERIAL        |
| pet_id          | FOREIGN KEY, NOT NULL   | SERIAL        |
| treatment       |                         | TEXT          |
| diagnosis        |                         | TEXT          |
| procedure      |                         | TEXT        |
| ImagenUrl           |                         | VARCHAR(250)   |
| dateOfAttention      | DEFAULT DATE_NOW        | DATE          |



## Swagger documentation:


[DRF SannaVet API: https://sannavet-api.onrender.com/swagger-ui/](https://sannavet-api.onrender.com/swagger-ui/)


## Sample ouput:

```json
{
    "id": 1,
    "username": "rosita",
    "email": "rosita@gmail.com",
    "first_name": "rosita",
    "last_name": "mucha yalo",
    "role": "cliente",
    "pets": [
      {
        "id": 1,
        "nombre": "rambo",
        "sexo": "m",
        "especie": "pero",
        "raza": "mixta",
        "color": "lomo caramelo, pecho blanco",
        "fotoUrl": "https://drfecommercee.s3.us-west-1.amazonaws.com/pets/rambo.png",
        "esterilizado": false,
        "peso": "4.0",
        "appoiments": [
          {
            "id": 7,
            "pet_id": 1,
            "veterinarian_id": 2,
            "date": "2024-02-28",
            "hour": "15:45:00",
            "description": "Revision general",
            "payed": false,
            "state": false,
            "created_at": "2024-02-23T20:47:55.092166-05:00"
          }
        ],
        "attentions": [
          {
            "id": 1,
            "pet_id": 1,
            "diagnosis": "parasitosis",
            "treatment": "medicamento anti parásito vía oral",
            "procedure": "Dar el medicamento 3 veces al día, inmediatamente después de la comidas, tiene que beber mucho líquidos.",
            "imageUrl": null,
            "dateOfAttention": "2024-02-27T00:01:33.462433-05:00"
          },
          {
            "id": 2,
            "pet_id": 1,
            "diagnosis": "vacuna anti tétano",
            "treatment": "herida abierta por un clavo",
            "procedure": "Se le aplica una vacuna anti Tétano y se recomienda limpiar la herida, no dejar que el perro lama la Herida",
            "imageUrl": null,
            "dateOfAttention": "2024-02-27T00:05:39.846815-05:00"
          },
          {
            "id": 3,
            "pet_id": 1,
            "diagnosis": "Baño Dominical",
            "treatment": "Baño preventivo anti-pulgas",
            "procedure": "Se recomienda que no ande suelto en la calle, sin supervisión, para que no se contagie de pulgas",
            "imageUrl": null,
            "dateOfAttention": "2024-02-27T00:07:45.066815-05:00"
          }
        ]
      },
      {
        "id": 3,
        "nombre": "booby",
        "sexo": "m",
        "especie": "perro",
        "raza": "mixta",
        "color": "lomo negro, pecho blanco",
        "fotoUrl": "https://drfecommercee.s3.us-west-1.amazonaws.com/pets/booby.png",
        "esterilizado": true,
        "peso": "8.6",
        "appoiments": [
          {
            "id": 8,
            "pet_id": 3,
            "veterinarian_id": 4,
            "date": "2024-03-08",
            "hour": "19:15:00",
            "description": "Inyeccion",
            "payed": false,
            "state": false,
            "created_at": "2024-02-23T20:49:03.607159-05:00"
          }
        ],
        "attentions": [
          {
            "id": 4,
            "pet_id": 3,
            "diagnosis": "Rabia Preventiva",
            "treatment": "Vacuna antirrábica, 1ra dosis",
            "procedure": "Se le coloca vacuna antirábica de manera preventica, es su primera dosis, en toda la vida del perro",
            "imageUrl": null,
            "dateOfAttention": "2024-02-27T00:14:01.517618-05:00"
          }
        ]
      }
    ]
  }
```

![](https://www.shutterstock.com/image-vector/animal-paw-print-vector-icon-260nw-1820447291.jpg)



# Appendix: 

    Something useful to remember

## Instalación y Activación de eentorno virtual:

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



```