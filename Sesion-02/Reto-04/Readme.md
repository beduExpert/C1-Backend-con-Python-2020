`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Reto-04
## Automatizando la ejecución de archivos SQL con Python

### OBJETIVO
Construir un script en Python para ejecutar instrucciones SQL por medio de archivos para el proyecto BeduTravels

#### REQUISITOS
1. Carpeta de repo actualizada
1. Usar la carpeta de trabajo `Sesion-01/Reto-04`
1. Usar el nuevo diagrama del modelo entidad-relación:

   ![Modelo entidad-relación](bedutravels-modelo-er.jpg)

#### DESARROLLO
1. Crear el script `sql2mysql.py` que reciba como parámetro el nombre de un archivo con extensión sql y ejecute las instrucciones en un servidor MariaDB para la base de datos BeduTravels.

   __Ejecutando el script con el archivo `sql/tablas-inicial.sql`:__

    ```bash
    Sesion-01/Reto-04 $ python sql2mysql.py sql/tablas-inicial.sql

    Se ha ejecutado el archivo sql/tablas-inicial.sql correctamente
    ```

    __Lista de los nuevos datos en las tablas:__

    ```bash
    Sesion-01/Reto-04 $ python lista-registros.py Usuario

    Tabla: Usuario
    --------------
    Id | Nombre  | Apellidos | Edad | Genero
     1 | Hugo    | Mac Rico  |   10 | M     
     2 | Paco    | Mac Rico  |   15 | M     
     3 | Daisy   | Mac Rico  |   18 | H     
     4 | Luis    | Mac Rico  |   19 | M     
     5 | Goku    | Saiyajin  |   47 | M     
     6 | Vegeta  | Saiyajin  |   50 | M     
     7 | Chabelo |           |  100 | M     
    --------------
    ```
    ***

__NOTA:__ No demores más de 5 mins en este reto, si no ...
