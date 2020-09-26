`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Reto-03
## Operación UPDATE: Modificando datos con Python y MariaDB

### OBJETIVO
Realizar la operación __UPDATE__ para un registro de una tabla con Python y MariaDB.

### REQUISITOS
1. Contar con los datos de conexión a la base de datos BeduTravels.

   __Host:__ localhost <br />
   __User:__ BeduTravels <br />
   __Password:__ BeduTravels <br />
   __Base de datos:__ BeduTravels

1. Contar con la tabla __Usuario__ creada y con datos muestra en la base de datos.

  ![Tabla Usuario](assets/tabla-usuario.jpg)

1. Usar la carpeta de trabajo `Sesion-01/Reto-03/`

### DESARROLLO
1. __OPERACIÓN UPDATE__ Crear el script `actualiza-usuario.py` y realizar las modificaciones en el script `modelomysql.py` para que se pueda modificar un registro a la tabla Usuario en la base de datos BeduTravels desde la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `modelomysql`.

   __Caso: Ejecutando el script sin argumentos__

   ```console
   Sesion-01/Reto-03 $ python actualiza-usuario.py
   Usage: actualiza-usuario.py [OPTIONS] ID NOMBRE APELLIDOS EDAD GENERO
   Try "actualiza-usuario.py --help" for help.

   Error: Missing argument "ID".
   ```

   __Caso: Actualiza un registro a la tabla Usuario en base al id__

   ```console
   Sesion-01/Reto-03 $ python lista-registros.py Usuario

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

   Sesion-01/Reto-03 $ python actualiza-usuario.py 7 None Lopez None None
   Se ha actualizado el registro (7, None, 'Lopez', None, None) a la tabla Usuario

   Sesion-01/Reto-03 $ python lista-registros.py Usuario
   Tabla: Usuario
   --------------
   Id | Nombre  | Apellidos | Edad | Genero
    1 | Hugo    | Mac Rico  |   10 | M     
    2 | Paco    | Mac Rico  |   15 | M     
    3 | Daisy   | Mac Rico  |   18 | H     
    4 | Luis    | Mac Rico  |   19 | M     
    5 | Goku    | Saiyajin  |   47 | M     
    6 | Vegeta  | Saiyajin  |   50 | M     
    7 | Chabelo | Lopez     |  100 | M     
   --------------
   ```
   ***

__Nota:__ Este reto se realiza en 15 mins.

__Sugerencia:__ Usar el script `agrega-usuario.py` como base.
