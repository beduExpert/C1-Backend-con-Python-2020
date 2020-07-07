[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a un Proyecto

### OBJETIVOS
- Crear un entorno virtual para el tú proyecto
- Instalar Django
- Aplicar los conceptos de rutas, vistas y plantillas creando una aplicación web para tú proyecto
- Poder mostrar cuando menos la página de inicio de tú proyecto usando Django.

#### REQUISITOS
1. Constar con la carpeta del repo actualizada.
1. Usar la carpeta de trabajo `Sesion-03/Postwork/Proyecto/`.
1. Activar el entorno virtual para tú proyecto.
1. Página de inicio maquetada del tú proyecto en la carpeta `Sesion-03/Postwork/public_html/`.

### DESARROLLO
1. Crear un entorno virtual para tú proyecto usando el comando:

   ```console
   Sesion-03/Postwork $ conda create --name ??? python=3.7
   ```

   __Dejar activo el entorno ??? para continuar:__

   ```console
   Sesion-03/Postwork $ conda activate ???
   [...]

   (???) Sesion-03/Postwork $
   ```
   ***

1. Crear el tú proyecto con Django y nos cambiamos a la carpeta del proyecto:

   ```console
   (???) Postwork $ django-admin startproject ???

   (???) Postwork $ tree ???
   ???
   ├── ???
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py

   (???) Postwork $ cd ???

   (???) Postwork/??? $
   ```
   ***

1. Crear la aplicación __mi_app__ con el comando:

   ```console
   (???) Postwork/??? $ python manage.py ???

   (???) Postwork/??? $ tree
   .
   ├── ???
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── mi_app
   │   ├── admin.py
   │   ├── apps.py
   │   ├── __init__.py
   │   ├── migrations
   │   │   └── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   └── views.py
   └── manage.py
   ```
   ***

1. Ejecutar el proyecto __???__ con:

   ```console
   (???) Postwork/??? $ python manage.py runserver
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).

   You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.

   June 19, 2019 - 10:38:22
   Django version 2.2.2, using settings '???.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.   
   ```

   __Nota:__ Como el servidor bloquea la terminal, vamos a dejar esta terminal aquí y para los siguiente comandos abrir otra terminal, activar el entorno virtual ??? y cambiarse a la carpeta de trabajo `Sesion-03/Postwork/???/`.
   ***

1. Agrega la aplicación __mi_app__ a la configuración en el archivo `???/???/settings.py`:

   ```python
   # Application definition

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'mi_app',
   ]   
   ```
   ***

1. Mapear la url `/` con las rutas generales del proyecto __???__ hacia las rutas de la aplicación __mi_app__

   ```
   url / -> ???/???/urls.py -> ???/mi_app/urls.py
   ```

   __En el archivo `???/???/urls.py` agregar lo siguiente:__

   ```python
   from django.contrib import admin
   from django.urls import path, include  # modificada

   urlpatterns = [
       ???
       path('admin/', admin.site.urls),
   ]
   ```

   En la vetana donde se está ejecutando el proyecto __???__ se puede observar el siguiente mensaje de error:

   ```console
   (???) Postwork/??? $ python manage.py runserver
   [...]
   File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
   ModuleNotFoundError: No module named 'mi_app.urls'
   ```
   Lo que indica que nos falta crear el archivo `urls.py` dentro de la carpeta `???/mi_app/`
   ***

1. Mapear la url `/` con las rutas de la aplicación __mi_app__

   ```
   url / -> ???/mi_app/urls.py -> ???/mi_app/views.py
   ```

   __Crear el archivo `???/mi_app/urls.py` con el siguiente contenido:__

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       ???,
   ]
   ```

   __Reiniciar Django para observar el resultado:__

   ```console
   [...]
   File "/home/rctorr/repos/Curso-Python-Expert/Sesion-03/Postwork/???/mi_app/urls.py", line 5, in <module>
     path('', views.index, name='index'),
   AttributeError: module 'mi_app.views' has no attribute 'index'
   ```
   Lo que indica que en el archivo `mi_app/views.py` no existe una función llamada `index`, así que toca agregar dicha función.
   ***

1. Agregar la función/vista `index` al archivo `???/mi_app/views.py` con el siguiente contenido:

   ```python
   from django.http import HttpResponse
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       ???
   ```

   __Nota: Si la aplicación Django no está iniciada, iniciarla en este momento y abrir la siguiente url en el navegador__

   http://127.0.0.1:8000

   __El resultado que deberías de observar es una página con un mensaje__
   ***

1. Haciendo uso de las plantillas de Django integrar la página de inicio maquetada que se encuentra en `public_html/index.html`.

   __Crear las carpetas `???/mi_app/templates/mi_app`:__

   ```console
   (???) Postwork/??? $ mkdir mi_app/templates
   (???) Postwork/??? $ mkdir mi_app/templates/mi_app
   ```

   __Copiar el archivo `public_html/index.html` dentro de la carpeta `???/mi_app/templates/mi_app/`:__

   ```console
   (???) Postwork/??? $ cp ../public_html/index.html mi_app/templates/mi_app/

   (???) Postwork/??? $ tree mi_app/templates/
   mi_app/templates/
   └── mi_app
       └── index.html
   ```

   __Modificar la función `index()` en el archivo `mi_app/views.py` para hacer uso de las plantillas (templates)__

   ```python
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       return render(request, "mi_app/index.html")
   ```
   Por omisión, Django busca los archivos html en la carpeta `proyecto/aplicacion/templates/aplicacion/`

   __El resultado en el navegador ya debería de mostrarse tú página de inicio, pero sin estilos e imágenes__
   ***

1. Agregando acceso a los archivos estáticos (ruta y vista)

   __Crear la carpeta `???/mi_app/static/mi_app/`:__

   ```console
   (???) Postwork/??? $ mkdir mi_app/static
   (???) Postwork/??? $ mkdir mi_app/static/mi_app
   ```

   __Copiar las carpetas de los archivos estáticos (css, fonts, images, js, etc.):__

   ```console
   (???) Postwork/??? $ cp -a ../public_html/css mi_app/static/mi_app/

   (???) Postwork/??? $ cp -a ../public_html/fonts mi_app/static/mi_app/

   (???) Postwork/??? $ cp -a ../public_html/images mi_app/static/mi_app/

   (???) Postwork/??? $ cp -a ../public_html/js mi_app/static/mi_app/

   Sesion-03/Postwork/??? $ tree -d 1 mi_app/static/mi_app/
   mi_app/static/mi_app/
   ├── css
   ├── fonts
   │   ├── bootstrap
   │   ├── icomoon
   │   └── themify-icons
   ├── images
   └── js
   ```

   __Finalmente hay que modificar la ruta en el archivo `index.html` para que usen el sistema de Django__

   Todas las url relativas o absolutas ahora tienen que ser absolutas e iniciar con `/static/mi_app/`, unos ejemplos se muestra a continuación:

   ```html
   <!-- Animate.css -->
   <link rel="stylesheet" href="/static/mi_app/css/animate.css">
   <!-- Icomoon Icon Fonts-->
   <link rel="stylesheet" href="/static/mi_app/css/icomoon.css">
   ```
   Remplazar todas las coincidencias.

   __Actualizar el navegador y entonces se debería de ver la página mostrada al inicio__

   Si no funciona:
   - Recargar la página forzado actualizar el cache del navegador con `Control+Shift+R`.
   - En la ventana donde se está ejecutando el proyecto, deternlo y volver a iniciarlo.
   - Usar una ventana de incógnito.
   - Pedir ayuda a un experto (que no vas a encontrar en clase!)

   Si si funciona entonces:
   - Misión cumplida!
