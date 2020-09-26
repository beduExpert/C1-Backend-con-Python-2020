`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-02

## Inicializando Django con MySQL

### OBJETIVOS
- Conocer el procedimiento para inicializar un servidor MySQL
- Conocer el procedimiento para inicializar la base de datos.
- Conocer el procedimiento para realizar una conexión a la base de datos con Django.

#### REQUISITOS
1. [Mysql 5.7 ](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)
1. [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) 
1. Contar con el repositorio actualizado creado por el experto para este módulo.
1. Abrir una terminal y posicionarse en la carpeta de trabajo

### DESARROLLO
1. En el Prework de la sesión identificamos cómo descargar e instalar MySQL en tu equipo y inicializarlo en nuestro sistema operativo, por lo cual iniciaremos nuestro gestor de base de datos.

2. Una vez inicializado realizaremos la conexión con __MySQL Workbench__ 

	![](img/1.png)

3. Procederemos a generar un nuevo Schema, al cual le asignaremos el nombre de base_MySQL

	![](img/2.png)
	![](img/3.png)
	![](img/4.png)

4. Para poder utilizar __MySQL__ en Django es necesario instalar un cliente para Python, por lo cual abriremos nuestro proyecto

	```console
   $ cd django
   ```
   
	![](img/5.png)
	
5. Recordemos que es importante activar nuestro entorno virtual

	```console
   $ source bin/activate
   ```
   ![](img/5.png)
   
6. Una vez activado procederemos a instalar __mysqlclient__ con el siguiente comando:

	```console
   $ pip3 install mysqlclient
   ```
   
7. A continuación conectaremos con nuestra base de datos, primero tendremos que configurar los parámetros con la base de datos que creamos anteriormente en el Workbench de MySQL. Abriremos el documento __Banco/Banco/settings.py__ y buscaremos el siguiente bloque de código:

	```python
   DATABASES = {
    	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    	}
	}
   ```
   
   ![](img/8.png)
   
8. Como lo vimos en el ejemplo anterior Django trabaja por defecto con SQLite3, por lo que tendremos que modificarlo para que tenga la información de la base de datos que queremos conectar.

	```python
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pruebamysql',
            'USER': 'nombreusuario',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
   ```
   
   ![](img/9.png)
   
9. Ya que tenemos todo configurado sólo queda realizar la migración de los modelos de la aplicación de Django. Abriremos nuestra terminal con el entorno activado y nos situaremos en la carpeta __banco__ seguido por el siguiente comando: 

	```console
   $ python3 manage.py migrate
   ```
   
10. Visualizaremos la siguiente pantalla la cual confirma la migración fue realizada con exito:

 	 ![](img/10.png)
 	 
11. Abriremos nuestro MySQLWorkbench y desplegaremos las tablas generadas por Django, comprobando que la configuración fue realizada con exito.

	![](img/11.png)
 


	

