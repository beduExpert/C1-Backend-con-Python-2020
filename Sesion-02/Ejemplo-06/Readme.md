`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-03
## Operación CREATE: Agregando datos con Python y MariaDB

### OBJETIVO
Conocer el procedimiento para realizar la operación __CREATE__ en una tabla con Python para el Ejemplo-03 Bibioteca.

### REQUISITOS
1. Contar con los datos de conexión a la base de datos Biblioteca.

   __Host:__ localhost
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

1. Contar con la tabla __Libro__ creada y con datos muestra en la base de datos:

  ![Tabla Libro](assets/tabla-libro.jpg)

1. Usar la carpeta de trabajo `Sesion-02/Ejemplo-06`

### DESARROLLO
1. __OPERACIÓN CREATE__ Crea el script `agrega-libro.py` y realiza las modificaciones en el script `modelomysql.py` para que se pueda agregar un nuevo registro a la tabla Libro en la base de datos Biblioteca desde la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `modelomysql`.

   __Caso: Ejecutando el script sin argumentos__

   ```console
   Sesion-02/Ejemplo-06 $ python agrega-libro.py
   Usage: agrega-libro.py [OPTIONS] TITULO EDITORIAL NUMPAG AUTORES
   Try "agrega-libro.py --help" for help.

   Error: Missing argument "TITULO".
  ```

   __Caso: Agregando un libro a la tabla__

   ```console
   Sesion-02/Ejemplo-06 $ python agrega-libro.py "Un puente hacia el infinito" "Zeta Bolsillo" 409 1
   Se ha agregado el registro ('Un puente hacia el infinito', 'Zeta Bolsillo', 409, '1') a la tabla Libro

   Sesion-02/Ejemplo-06 $ python lista-registros.py Libro

   Tabla: Libro
   --------------
   Id | Titulo                      | Editorial     | Numpag | Autores
    1 | Yo, Robot                   | Gnome Press   |    374 |       1
    2 | El fin de la eternidad      | Gnome Press   |    191 |       1
    3 | El arte de la guerra        | Obelisco      |    112 |       2
    4 | Un puente hacia el infinito | Zeta Bolsillo |    409 |       1
   --------------
   ```
   ***

__Nota:__ Este reto se realiza en 15 mins.
