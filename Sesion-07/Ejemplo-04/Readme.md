[`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Ejemplo-04
## Archivos estáticos y base de datos en producción

### OBJETIVOS
- Preparar el entorno de producción para los archivos estáticos
- Configurar la base de datos en producción

### REQUISITOS
1. Actualizar repositorio __Backend-con-Python__
1. La carpeta de referencia es `Sesion-07/Ejemplo-04/Bedutravels/`
1. Contar con repo __Bedutravels__ en equipo local
1. La carpeta de trabajo debe ser `Bedutravels/`
1. Contar con repo __Bedutravels__ en Github
1. Contar con repo __Bedutravels__ en Pythonanywhere
1. Contar con el proyecto ya configurado en Pythonanywhere

### DESARROLLO
1. Nuestra aplicación en producción actualmente se ve sin estilos y para corregir esto en la carpeta `Bedutravels/` en el equipo local agregar el siguiente código al archivo `Bedutravels/Bedutravels/settings-prod.py`:

   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, "static")
   ```

   __Agregar el cambio a repo local con:__
   ```console
   Bedutravels $ git add Bedutravels/settings-prod.py
   Bedutravels $ git commit -m "Agregando variable STATIC_ROOT a settings-prod.py"
   [master 24fa423] Agregando variable STATIC_ROOT a settings-prod.py
   1 file changed, 1 insertion(+)
   Bedutravels $
   ```

   __Actualizando el repo en github con:__
   ```console
   Bedutravels $ git push
   Username for 'https://github.com': tu-usuario
   Password for 'https://rctorr@github.com':
   Counting objects: 4, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (4/4), done.
   Writing objects: 100% (4/4), 408 bytes | 0 bytes/s, done.
   Total 4 (delta 3), reused 0 (delta 0)
   remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
   To https://github.com/rctorr/Bedutravels.git
      d3d73e1..24fa423  master -> master

   Bedutravels $
   ```

   __Actualizando el repo en Pythonanywhere en un consola bash:__
   ```console
   (Bedutravels) 20:34 ~/Bedutravels (master)$ git pull                                               remote: Enumerating objects: 7, done.
   remote: Counting objects: 100% (7/7), done.
   remote: Compressing objects: 100% (1/1), done.
   remote: Total 4 (delta 3), reused 4 (delta 3), pack-reused 0
   Unpacking objects: 100% (4/4), done.                                              From https://github.com/rctorr/Bedutravels
    d3d73e1..24fa423  master     -> origin/master
   Updating d3d73e1..24fa423                                       
   Fast-forward                                                           Bedutravels/settings-prod.py | 1 +               
     1 file changed, 1 insertion(+)                               
   (Bedutravels) 20:38 ~/Bedutravels (master)$
   ```

   __En Pythonanywhere se crea la carpeta `Bedutravels/static` y se actualizan los archivos estáticos:__
   ```console
   (Bedutravels) 20:51 ~/Bedutravels (master)$ mkdir static
   (Bedutravels) 20:51 ~/Bedutravels (master)$ python manage.py collectstatic

   195 static files copied to '/home/rctorr/Bedutravels/static'.
   (Bedutravels) 20:52 ~/Bedutravels (master)$
   ```

   __En Pythonanywhere en Dashboard - Web sección Static se agregar la ruta para los archivos estáticos:__

   ![Configurando archivos estáticos](assets/produccion-01.png)

   __Recargar la aplicación dando click en reload en el Dashboard - Web__

   Y finalmente actualiza la página en el navegador y el resultado debería ser similar al siguiente:
   ![Aplicación con estilos](assets/produccion-02.png)

1. La base de datos a usar en producción es MySQL con los datos obtenidos anteriormente, se configuran en el archivo `Bedutravels/Bedutravels/settings-prod.py` en la sección de base de datos quedando de la siguiente forma:

   ```python
   # Database
   # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'rctorr$Bedutravels',
           'USER': 'rctorr',
           'PASSWORD': 'pythonsql',
           'HOST': 'rctorr.mysql.pythonanywhere-services.com',
       }
   }   
   ```

   __Nuevamente se realizar el proceso de actualizar el repo local, el repo en github:__

   ```console
   Bedutravels $ git add Bedutravels/settings-prod.py
   Bedutravels $ git commit -m "Agregando configuración para hacer uso de MySQL como base de datos en settings-prod.py"
   [master b1026f1] Agregando configuración para hacer uso de MySQL como base de datos en settings-prod.py
    1 file changed, 5 insertions(+), 2 deletions(-)

   Bedutravels $ git push
   Username for 'https://github.com': rctorr
   Password for 'https://rctorr@github.com':
   Counting objects: 4, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (4/4), done.
   Writing objects: 100% (4/4), 507 bytes | 0 bytes/s, done.
   Total 4 (delta 3), reused 0 (delta 0)
   remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
   To https://github.com/rctorr/Bedutravels.git
      24fa423..b1026f1  master -> master
   ```

   __Actualizando el repo en producción:__
   ```console
   (Bedutravels) 21:37 ~/Bedutravels (master)$ git pull    
   remote: Enumerating objects: 7, done.
   remote: Counting objects: 100% (7/7), done.
   remote: Compressing objects: 100% (1/1), done.
   remote: Total 4 (delta 3), reused 4 (delta 3), pack-reused 0
   Unpacking objects: 100% (4/4), done.                   
   From https://github.com/rctorr/Bedutravels
      24fa423..b1026f1  master     -> origin/master
   Updating 24fa423..b1026f1
   Fast-forward
    Bedutravels/settings-prod.py | 7 +++++--
    1 file changed, 5 insertions(+), 2 deletions(-)

   (Bedutravels) 21:37 ~/Bedutravels (master)$
   ```

   Como se ha configurado la base de datos MySQL para producción por lo que se necesitará el módulo correspondiente para que Django pueda realizar la conexión:

   ```console
   (Bedutravels) 21:37 ~/Bedutravels (master)$ pip install mysqlclient
   Looking in links: /usr/share/pip-wheels
   Collecting mysqlclient
     Downloading https://files.pythonhosted.org/packages/f4/f1/3bb6f64ca7a429729413e6556b7ba5976df06019a5245a43d36032f1
   061e/mysqlclient-1.4.2.post1.tar.gz (85kB)
        |████████████████████████████████| 92kB 3.0MB/s
   Building wheels for collected packages: mysqlclient
     Building wheel for mysqlclient (setup.py) ... done
     Created wheel for mysqlclient: filename=mysqlclient-1.4.2.post1-cp37-cp37m-linux_x86_64.whl size=97680 sha256=ef87
   85eae5003285fc98d4bc24f2b211eeebe85cf0c99795550c2c1a2118fad6
     Stored in directory: /home/rctorr/.cache/pip/wheels/30/91/e0/2ee952bce05b1247807405c6710c6130e49468a5240ae27134
   Successfully built mysqlclient
   Installing collected packages: mysqlclient
   Successfully installed mysqlclient-1.4.2.post1

   (Bedutravels) 21:37 ~/Bedutravels (master)$
   ```

   Como tenemos una nueva base de datos, ésta está vacía por lo que hay que aplicar las migraciones en producción y luego crear el usuario administrador de nuestra aplicación.
   ```console
   (Bedutravels) 21:37 ~/Bedutravels (master)$ python manage.py migrate
   System check identified some issues:

   WARNINGS:
   ?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
   HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertio
   n, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.c
   om/en/2.2/ref/databases/#mysql-sql-mode
   Operations to perform:
   Apply all migrations: admin, auth, catalogo, contenttypes, sessions
   Running migrations:
   Applying contenttypes.0001_initial... OK
   Applying auth.0001_initial... OK
   Applying admin.0001_initial... OK
   Applying admin.0002_logentry_remove_auto_add... OK
   Applying admin.0003_logentry_add_action_flag_choices... OK
   Applying contenttypes.0002_remove_content_type_name... OK
   Applying auth.0002_alter_permission_name_max_length... OK
   Applying auth.0003_alter_user_email_max_length... OK
   Applying auth.0004_alter_user_username_opts... OK
   Applying auth.0005_alter_user_last_login_null... OK
   Applying auth.0006_require_contenttypes_0002... OK
   Applying auth.0007_alter_validators_add_error_messages... OK
   Applying auth.0008_alter_user_username_max_length... OK
   Applying auth.0009_alter_user_last_name_max_length... OK
   Applying auth.0010_alter_group_name_max_length... OK
   Applying auth.0011_update_proxy_permissions... OK
   Applying catalogo.0001_initial... OK
   Applying catalogo.0002_libro... OK
   Applying catalogo.0003_prestamo... OK
   Applying catalogo.0004_prestamo_libros... OK
   Applying catalogo.0005_remove_prestamo_libros... OK
   Applying catalogo.0006_prestamo_libros... OK
   Applying sessions.0001_initial... OK

   (Bedutravels) 21:58 ~/Bedutravels (master)$ python manage.py createsuperuser
   Nombre de usuario (leave blank to use 'rctorr'): bedutravels
   Dirección de correo electrónico: bedutravels@gmail.com
   Password:
   Password (again):
   La contraseña es muy similar a  nombre de usuario.
   Bypass password validation and create user anyway? [y/N]: y
   Superuser created successfully.

   (Bedutravels) 21:58 ~/Bedutravels (master)$
   ```

   __En el Dashboard - Web dar click en el botón de reload__

   Actualizar el navegador y se debería obtener el siguiente resultado:
   ![Aplicación con nueva base de datos MySQL](assets/produccion-03.png)

   Esto es así porque la base de datos en producción está vacía, así que es necesario agregar datos mediante el panel de adminitrador de Django o se pueden cargar los datos del archivo `datos/tours.json` desde la __Consola Bash en el Dashboard__.

   Para ellos, lo primero es agregar el archivos tours.json al repo local __Bedutravles__:

   ```console
   (Bedutravels) Bedutravels (master)$ cp -a Backend-con-Python/Sesion-07/datos .
   (Bedutravels) Bedutravels (master)$ git add .
   (Bedutravels) Bedutravels (master)$ git commit -m "Agregando datos"
   (Bedutravels) Bedutravels (master)$ git push
   Username for 'https://github.com': rctorr
   Password for 'https://rctorr@github.com':
   Contando objetos: 4, listo.
   Delta compression using up to 4 threads.
   Comprimiendo objetos: 100% (3/3), listo.
   Escribiendo objetos: 100% (4/4), 1.13 KiB | 1.13 MiB/s, listo.
   Total 4 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/rctorr/Bedutravels.git
      cef36d7..fc80726  master -> master
   ```

   En el repo de Pythonanywhere, actualizar el repo e importar los datos:

   ```console
   (Bedutravels) 18:51 ~/Bedutravels (master)$ git pull
   (Bedutravels) 18:51 ~/Bedutravels (master)$ pwd
   /home/rctorr/Bedutravels
   (Bedutravels) 18:51 ~/Bedutravels (master)$ python manage.py loaddata datos/tours.json
   Installed 20 object(s) from 1 fixture(s)

   (Bedutravels) 18:51 ~/Bedutravels (master)$
   ```

   Tras lo cual recargar el navegador para obtener algo similar a lo siguiente:
   ![Aplicación con datos](assets/produccion-04.png)

__Misión cumplida, ya tenemos nuestro proyecto en Producción con archivos estáticos disponibles y base de datos configurada y poblada.__
