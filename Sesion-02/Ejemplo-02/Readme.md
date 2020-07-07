`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-02
## Operación READ: Lectura de datos con Python y MariaDB

### OBJETIVO
Conocer el procedimiento para realizar la operación __Read__ a una tabla en un servidor MariaDB desde Python para el proyecto Biblioteca.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos Biblioteca.

   __Host:__ localhost <br />
   __User:__ Biblioteca <br />
   __Password:__ Biblioteca <br />
   __Base de datos:__ Biblioteca

1. Usar la carpeta de trabajo `Sesion-01/Ejemplo-02`

1. Contar con la tabla __Libro__ creada y con los datos contenidos en el archivo `sql/tabla-libro.sql`.

   ![Tabla Libro](assets/tabla-libro.jpg)

   Si no cuenta con la tabla, entonces inicializarla con el siguiente comando:
   ```console
   Sesion-01/Ejemplo-02 $ docker exec -i pythonsql mysql -hlocalhost -uBiblioteca -pBiblioteca Biblioteca < sql/tabla-libro.sql

   Sesion-01/Ejemplo-02 $
   ```

1. Instalar el módulo `mysql-connector-python` que será el responsable de permitir realizar una conexión a base de datos MySQL / MariaDB desde Python.

   __Sito principal:__
   https://dev.mysql.com/doc/connector-python/en/

   __Instalación con el comando pip:__
   ```console
   $ pip install mysql-connector-python
   Collecting mysql-connector-python
   Using cached https://files.pythonhosted.org/packages/43/bd/43a128bbd6a3237d6f255c7afaa9308430d5c90f8db8371276169722f037/mysql_connector_python-8.0.16-cp37-cp37m-manylinux1_x86_64.whl
   Requirement already satisfied: protobuf>=3.0.0 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from mysql-connector-python) (3.7.1)
   Requirement already satisfied: six>=1.9 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (1.12.0)
   Requirement already satisfied: setuptools in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (41.0.0)
   Installing collected packages: mysql-connector-python
   Successfully installed mysql-connector-python-8.0.16

   $
   ```

### DESARROLLO
 1. __OPERACIÓN READ__ Crea el script `lista-registros.py` que imprima en formato texto en la salida estándar, la lista de registros de la tabla proporcionada como parámetro en la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `stdout`.

 Aplicar el modelo MVC y todas las funciones que tengan que ver con la base de datos colocarlas dentro del script/módulo `modelomysql.py`.

   __Caso: Ejecutando el script sin argumentos__

   ```console
   Sesion-01/Ejemplo-02 $ python lista-registros.py

   Tablas disponibles
   ------------------
   Libro
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla Libro__

   ```console
   Sesion-01/Ejemplo-02 $ python lista-registros.py Libro

   Tabla: Libro
   ------------
   Id | Titulo                 | Editorial   | NumPag | Autores
    1 | Yo, Robot              | Gnome Press |    374 |       1
    2 | El fin de la eternidad | Gnome Press |    191 |       1
    3 | El arte de la guerra   | Obelisco    |    112 |       2
   ------------
   ```
   ***

__Nota:__ En la carpeta ya existe el script `stdout.py` que es un módulo que contiene la función `imprime_registros()` y se puede hacer uso de ella.
