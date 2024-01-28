Table "Usuario" {
  "UsuarioID" SERIAL [pk, increment]
  "Nombre" VARCHAR(50) [not null]
  "Apellido" VARCHAR(50) [not null]
  "email" VARCHAR(100) [not null]
  "password" VARCHAR(100) [not null]
  "is_staff" BOOLEAN [default: FALSE]
  "is_active" BOOLEAN [default: TRUE]
}

Table "Mascota" {
  "MascotaID" SERIAL [pk, increment]
  "UsuarioID" INTEGER [not null]
  "Nombre" VARCHAR(50) [not null]
  "Sexo" "CHAR (1)" [not null]
  "Especie" VARCHAR(50) [not null]
  "Raza" VARCHAR(50) [not null]
  "Color" VARCHAR(50) [not null]
  "FotoUrl" VARCHAR(200) [default: "example.com"]
  "Esterilizado" BOOLEAN [not null]
  "Peso" DECIMAL(5,2) [default: 2.0]
}

Table "Citas" {
  "CitaID" SERIAL [pk, increment]
  "MascotaID" INTEGER [not null]
  "VeterinarioID" INTEGER
  "Fecha" DATE [not null]
  "Hora" TIME [not null]
  "Descripcion" TEXT
  "CitaPagada" BOOLEAN [default: FALSE]
  "Estado" BOOLEAN [default: FALSE]
  "CreateDate" DATE [default: `CURRENT_DATE`]
}

Table "Atenciones" {
  "AtencionID" SERIAL [pk, increment]
  "MascotaID" INTEGER [not null]
  "Diagnostico" TEXT
  "Tratamiento" TEXT
  "Procedimiento" TEXT
  "ImagenUrl" VARCHAR(250)
  "FechaAtencion" DATE [default: `CURRENT_DATE`]
}

Table "Veterinario" {
  "VeterinarioID" SERIAL [pk, increment]
  "Nombre" VARCHAR(50) [not null]
  "Apellido" VARCHAR(50) [not null]
  "email" VARCHAR(100) [not null]
  "password" VARCHAR(100) [not null]
  "is_staff" BOOLEAN [default: TRUE]
  "is_active" BOOLEAN [default: TRUE]
}

Table "CurrentAtentions" {
  "AtencionID" SERIAL [pk, increment]
  "MascotaID" INTEGER [not null]
  "VeterinarioID" INTEGER
  "EstadoAtencion" BOOLEAN [default: FALSE]
  "Fecha" DATE [default: `CURRENT_DATE`]
}

Ref:"Usuario"."UsuarioID" < "Mascota"."UsuarioID"

Ref:"Mascota"."MascotaID" < "Citas"."MascotaID"

Ref:"Veterinario"."VeterinarioID" < "Citas"."VeterinarioID"

Ref:"Mascota"."MascotaID" < "Atenciones"."MascotaID"

Ref:"Mascota"."MascotaID" < "CurrentAtentions"."MascotaID"

Ref:"Veterinario"."VeterinarioID" < "CurrentAtentions"."VeterinarioID"
