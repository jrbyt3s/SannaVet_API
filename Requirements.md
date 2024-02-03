Quiero que asumas el roll de un arquitecto de bases de datos para diseñar y construir el diagrama de entidad y relación de un sistema de gestión veterinaria con los siguientes requisitos:

Quiero que asumas el roll de un arquitecto de bases de datos. Yo necesito construir un sistema de gestión de verinaria con los siguientes requisitos:

## ROLES:
- USUARIO
- VETERINARIO
- ADMINISTRADOR.


## FUNCIONALIDADES PARA EL USUARIO:
- El usuario debe poder hacer login o registrarse en caso que no tenga una cuenta.
- Cada usuario puede registrar todas su mascotas.
- En el registro de la mascota se le puede adicionar los campos como el nombre, sexo, especie, raza, color, foto de perfil, esterilizado (si/no), peso.
- El usuario puede agendar citas para cada una de las mascotas.
- Las citas tendrán un campo de estado con los valores de: Confirmado / Cancelado
- El usuario puede adjuntar imágenes de las dolencias de su mascota al sacar una cita.
- El usuario sólo puede ver el registro de todas las atenciones de sus mascotas registradas en su cuenta.
- El usuario puede subir una imagen de perfil de la mascota.
- El usuario sólo puede ver sus mascotas.
- El usuario puede pagar la cita, para ello se usará el API de Mercado Pago.
- Las citas contarán con un campo para indicar si la cita fue pagada o no ha sido pagada.


## Tabla de Atenciones:
- La tabla de atenciones lleva un registro de las veces que la mascota fue atendido.
- A cada mascota se le asigna un registro de atención cada vez que se atiende en la veterinaria.
- La tabla de atenciones guarda el registro de cada atención realizada en la veterinaria.
- La tabla de atenciones guarda el diagnóstico de cada mascota
- La tabla de atenciones guarda el tratamiento de cada mascota
- La tabla de atenciones guarda el procedimiento realizado como Rayos-X, ecografías, exámenes de sangre
- La tabla de atenciones puede guardar imágenes de las dolencias de la mascota por ejemplo foto de sarna, alergia, etc.
- La tabla de atenciones debe guardar la fecha de atención.



## FUNCIONALIDAD GENERAL:
 El sistema tiene una tabla de currerent_atentions el cual muestra el estado de la atencion de las mascotas que vayan haciendo checking presencial en la veterinaria. esta tabla tiene información de la mascota que hizo checking y el estado de: atendiendo/en_cola. En la tabla currerent_atentions se podrá guardar al médico veterinario que va atender a la mascota y también guardar la fecha de la atención en forma autonática.

## FUNCIONALIDADES PARA EL VETERINARIO:
 - El veterinario puede ver la tabla de citas del día.
 - El Veterinario puede ver si la cita está pagada.
 - El veterinario puede hacer el checking a las citas confirmadas de manera presencial, haciendo que la mascota se muestre en la tabla current_atencions.
 - El veterinario puede agregar / actualizar la tabla de atenciones de cada mascota.
 - El veterinario puede agregar / actualizar  fotos de dolencias de la mascota (por ejemplo foto de sarna, alergia, etc.) a la tabla atenciones.
 - El veterinario puede agregar procedimientos como Rayos-X, ecografías, exámenes de sangre, orina a la tabla atenciones.
 - En la tabla atenciones se podrá guardar los tratamientos.
 - En la tabla atenciones se podrá guardar la fecha de la atención en forma autonática.






Generate mermaind code for sequence diagram for this case

...
Relaciones:

Usuario - Mascota (1:N): Un usuario puede tener varias mascotas, pero cada mascota pertenece a un único usuario.
Usuario - Cita (1:N): Un usuario puede tener varias citas, pero cada cita pertenece a un único usuario.
Mascota - Cita (1:N): Una mascota puede tener varias citas, pero cada cita pertenece a una única mascota.
Mascota - HistoriaClinica (1:1): Cada mascota tiene una única historia clínica.
Mascota - CurrentAtentions (1:1): Cada mascota puede tener una atención actual en la veterinaria.
Veterinario - Cita (1:N): Un veterinario puede tener varias citas, pero cada cita tiene un único veterinario.
Veterinario - CurrentAtentions (1:N): Un veterinario puede atender a varias mascotas, pero cada atención tiene un único veterinario.
HistoriaClinica - Procedimiento (N:M): Una historia clínica puede tener varios procedimientos y un procedimiento puede estar asociado a varias historias clínicas.
HistoriaClinica - Imágenes (N:M): Una historia clínica puede tener varias imágenes y una imagen puede estar asociada a varias historias clínicas.


# Usuario


| Column Name        | constraint   | Data Type    |
|--------------------|--------------|--------------|
| UsuarioID          | PRIMARY KEY  | SERIAL       |
| Nombre             | NOT NULL     | VARCHAR(50)  |
| Apellido           | NOT NULL     | VARCHAR(50)  |
| email              | NOT NULL     | VARCHAR(100) |
| password           | NOT NULL     | VARCHAR(100) |
| is_staff           | DEFAULT FALSE | BOOLEAN     |
| is_active          | DEFAULT TRUE | BOOLEAN      |
| roll               | DEFAUL 'CLIENT'| VARCHAR(20) |
| ...                |              |


**Relaciones:**
 -Usuario - Mascota (1:N): Un usuario puede tener varias mascotas, pero cada mascota pertenece a un único usuario.
 -Usuario - Cita (1:N): Un usuario puede tener varias citas, pero cada cita pertenece a un único usuario.




# Mascota


| Column Name   | Constraint            | Data Type     |
|---------------|-----------------------|---------------|
| MascotaID     | PRIMARY KEY           | SERIAL        |
| UsuarioID     | FOREIGN KEY, NOT NULL | SERIAL        |
| Nombre        | NOT NULL              | VARCHAR(50)   |
| Sexo          | NOT NULL              | CHAR(1)       |
| Especie       | NOT NULL              | VARCHAR(50)   |
| Raza          | NOT NULL              | VARCHAR(50)   |
| Color         | NOT NULL              | VARCHAR(50)   |
| FotoUrl       | DEFAULT "example.com" | VARCHAR(200)   |
| Esterilizado  | NOT NULL              | BOOLEAN       |
| Peso          | DEFAULT 2.0           | DECIMAL(5,2)  |




**Relaciones:**
- Mascota - Cita (1:N): Una mascota puede tener varias citas, pero cada cita pertenece a una única mascota.
- Mascota - Atenciones (1:N): Una mascota puede tener varias Atenciones, pero cada atencion pertenece a una única mascota.
- Mascota - CurrentAtentions (1:1): Cada mascota puede tener una atención actual en la veterinaria.




# Citas


| Column Name   | Constraint            | Data Type     |
|---------------|-----------------------|---------------|
| CitaID        | PRIMARY KEY           | SERIAL        |
| MascotaID     | FOREIGN KEY, NOT NULL | SERIAL        |
| VeterinarioID | FOREIGN KEY           | SERIAL        |
| Fecha         | NOT NULL              | DATE          |
| Hora          | NOT NULL              | TIME          |
| descripcion   |                       | TEXT          |
| CitaPagada    | DEFAULT FALSE         | BOOLEAN       |
| estado        | DEFAULT FALSE         | BOOLEAN       |                      
| create_date   | DEFAULT DATE_NOW      | DATE          |








# Atenciones


| Column Name         | Constraint              | Data Type     |
|-------------------- |-------------------------|---------------|
| AtencionID   | PRIMARY KEY             | SERIAL        |
| MascotaID           | FOREIGN KEY, NOT NULL   | SERIAL        |
| Diagnóstico         |                         | TEXT          |
| Tratamiento         |                         | TEXT          |
| Procedimiento       |                         | TEXT        |
| ImagenUrl           |                         | VARCHAR(250)   |
| FechaAtencion       | DEFAULT DATE_NOW        | DATE          |




# Veterinario


| Column Name     | Constraint      | Data Type    |
|-----------------|-----------------|--------------|
| VeterinarioID   | PRIMARY KEY     | SERIAL       |
| Nombre          | NOT NULL        | VARCHAR(50)  |
| Apellido        | NOT NULL        | VARCHAR(50)  |
| email           | NOT NULL        | VARCHAR(100) |
| password        | NOT NULL        | VARCHAR(100) |
| is_staff        | DEFAULT TRUE    | BOOLEAN       |
| is_active       | DEFAULT TRUE   | BOOLEAN       |




**Relaciones:**
Veterinario - Cita (1:N): Un veterinario puede tener varias citas, pero cada cita tiene un único veterinario.
Veterinario - CurrentAtentions (1:N): Un veterinario puede atender a varias mascotas, pero cada atención tiene un único veterinario.


# CurrentAtentions


| Column Name    | Constraint            | Data Type     |
|----------------|-----------------------|---------------|
| AtencionID     | PRIMARY KEY           | SERIAL        |
| MascotaID      | FOREIGN KEY, NOT NULL | SERIAL        |
| VeterinarioID  | FOREIGN KEY           | SERIAL        |
| EstadoAtencion | DEFAULT FALSE         | BOOLEAN       |
| Fecha          | DEFAULT DATE_NOW      | DATE          |
| ...            |                       |               |




**Relaciones:**
Mascota - CurrentAtentions (1:N): Una Mascota puede tener múltiples atenciones actuales, pero cada antencion actual tiene a única mascota.
