`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Reto-01

## Inicializando un servidor MariaDB y una base de datos haciendo uso de contenedores

### OBJETIVO
Inicializar la base de datos en un servidor MariaDB haciendo uso de contenedores para el proyecto BeduTravels.

#### REQUISITOS
1. Contar con Docker instalado
1. Contar con el contenedor __pythonsql__ ya creado en el Ejemplo-01.
1. Contar con los datos de conexión al servidor MariaDB como usuario root:
  - __Host:__ localhost
  - __User:__ root
  - __Pass:__ pythonsql
1. Haber actualizado el repositorio
1. Abrir una terminal y cambiarse a la carpeta de trabajo `Sesion-02/Reto-01`:

   ```console
   $ cd Sesion-02/Reto-01

   Sesion-02/Reto-01 $
   ```

### DESARROLLO
4. Inicializar la base de datos usando el archivo `sql/banco.sql`:

   ```console
   Sesion-02/Reto-01 $ docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < banco.sql
   ```
   ***

7. Para validar que la base de datos se haya inicializado de forma correcta se realiza una conexión a la base de datos Banco usando los datos:

   - __Host:__ localhost
   - __User:__ Banco
   - __Pass:__ Banco
   - __Base de datos:__ Banco

  ```console
  Sesion-02/Reto-01 $ docker exec -it pythonsql mysql -hlocalhost -uBanco -pBanco Banco
  Welcome to the MariaDB monitor.  Commands end with ; or \g.
  Your MariaDB connection id is 11
  Server version: 10.3.15-MariaDB-1:10.3.15+maria~bionic mariadb.org binary distribution

  Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

  MariaDB [Banco]> EXIT;

  Sesion-02/Reto-01 $
  ```
  ***
  
  ![](img/1.png)

Si has llegado hasta este punto __FELICIDADES__, toma __otro__ respiro o ayuda a algún compañero que no lo haya logrado aún o tomate un café te lo mereces.
