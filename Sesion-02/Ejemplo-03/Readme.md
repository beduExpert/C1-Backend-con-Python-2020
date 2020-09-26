`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-03

## Inicializando Django con PostgreSQL

### OBJETIVOS
- Conocer el procedimiento para inicializar un servidor PostgreSQL
- Conocer el procedimiento para inicializar la base de datos.
- Conocer el procedimiento para realizar una conexión a la base de datos con Django.

#### REQUISITOS
1. [PostgreSQL](https://www.postgresql.org)
1. Contar con el repositorio actualizado creado por el experto para este módulo.
1. Abrir una terminal y posicionarse en la carpeta de trabajo

### DESARROLLO
1. En el Prework de la sesión identificamos cómo descargar e instalar __PostgreSQL__ en tu equipo y inicializarlo en nuestro sistema operativo, por lo cual iniciaremos nuestro gestor de base de datos.
	
	![](img/1.png)
	![](img/2.png)

2. Procederemos a generar una nueva base de datos, al cual le asignaremos el nombre de __pruebapostgres__

	![](img/3.png)
	![](img/4.png)
	![](img/5.png)

	

4. Para poder utilizar __PostgreSQL__ en Django es necesario instalar un cliente para Python, por lo cual abriremos nuestro proyecto. Recordemos que es importante activar nuestro entorno virtual

	```console
   $ cd django
   ```
   ```console
   $ source bin/activate
   ```
   
	![](img/6.png)
	
   
6. Una vez activado procederemos a instalar __psycopg2__ con el siguiente comando:

	```console
   $ pip install psycopg2-binary
   ```
   
   ![](img/7.png)
   
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
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pruebapostgres',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
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
 	 
11. Abriremos nuestro gestor y desplegaremos las tablas generadas por Django, comprobando que la configuración fue realizada con exito.

	![](img/11.png)
 


	

