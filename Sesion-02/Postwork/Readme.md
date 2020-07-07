`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Postwork
## Bases de datos relacionales con Python y MariaDB aplicado a tú Proyecto

### OBJETIVOS
- Inicializar un servidor MariaDB y la base de datos para tú Proyecto haciendo uso de contenedores.
- Realizar operaciones de CRUD datos con Python y MariaDB
- Automatizando la ejecución de archivos SQL con Python
- Obtener un reporte de datos a partir de una base de datos relacional en MariaDB usando Python.

### REQUISITOS
1. Contar con Docker instalado.
1. Contar con el archivo `Sesion-01/Postwork/sql/proyecto.sql` con la definición la base de datos, usuario y permisos para tú Proyecto.
1. Contar con el archivo `Sesion-01/Postwork/sql/tablas.sql` con la definición de las tablas de tú Proyecto.
1. Contar con el diagrama del modelo entidad-relación de tú Proyecto
1. Usar la carpeta de trabajo `Sesion-01/Postwork`
1. Los datos de administrador del servidor MariaDB:

   __Host:__ localhost<br />
   __User:__ root<br />
   __Pass:__ pythonsql

### DESARROLLO
1. __INICIALIZAR LA BASE DE DATOS__ Este paso es muy similar al realizado en el Reto-01, sólo que ahora se usará el archivo `sql/proyecto.sql`.

  __Comando a ejecutar para el caso de Docker en Linux o Mac:__
  ```sh
  Sesion-01/Postwork $ sudo docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de Docker en Windows:__
  ```sh
  Sesion-01/Postwork > docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de MySQL:__
  ```sh
  Sesion-01/Postwork $ mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```
  ***

1. __INICIALIZACIÓN DE TABLAS__ Las tablas se pueden crear usando el archivo `sql/tablas-proyecto.sql` con el siguiente comando:

   ```console
   Sesion-01/Postwork $ sudo docker exec -i pythonsql mysql -hlocalhost -uProyecto -pProyecto Proyecto < sql/tablas.sql

   Sesion-01/Postwork $
   ```
   Asumiendo que los datos de acceso para la base de datos para tú proyecto son:

   __Host:__ localhost<br />
   __User:__ Proyecto<br />
   __Pass:__ Proyecto<br />
   __Base:__ Proyecto   
   ***

1. __AUTOMATIZANDO__ Otra opción para inicializar la base de datos o las tablas es que copies y modifiques en caso de ser necesario el script `sql2mysql.py` con el cual podrás ejecutar los archivos sql, por ejemplo:

   __Para inicializar las tablas:__
   ```console
   Sesion-01/Postwork $ python sql2mysql.py sql/tablas.sql

   Sesion-01/Postwork $
   ```

1. __OPERACIONES CRUD__ Modifica o crea los script necesarios para poder realizar las operaciones que necesites, por ejemplo `lista-registros.py`, `agrega-registro.py`, `actualiza-registro` o `borra-registro`.

   __Caso: Ejecutando el script `lista-registros.py` sin argumentos__

   ```console
   Sesion-01/Postwork $ python lista-registros.py

   Tablas disponibles
   ------------------
   ???
   ???
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla ???__

   ```console
   Sesion-01/Postwork $ python lista-registros.py ???

   Tabla: ???
   --------------
   ???
   --------------
   ```
   ***

1. __GENERANDO REPORTES__ Para este paso seguir las instrucciones del Proyecto realizado en clase pero ahora con los datos para tú Proyecto, crea el script llamado `lista-reporte.py` que muestre resultados de dos o más tablas y que sea información útil.

  __Resultado de ejecución del script:__
  ```console
  Clase-06/Postwork $ python lista-reporte.py
  [Tabla con renglones resultado ...]
  ```
  ***

### SUGERENCIAS
 - Recuerda que cuentas con los scripts `stdout.py`, `modelomysql.py`, `lista-registros.py` a tu disposición.
 - También cuentas con los script `agrega-nombretabla.py` o `lista-reporte.py` que contienen el código mínimo para que puedas modificarlos o complementarlo para tus propios fines.
