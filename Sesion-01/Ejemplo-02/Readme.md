[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo-02
## Iniciar la construcción de una aplicación web con Django

### OBJETIVOS
- Conocer como iniciar un proyecto en Django
- Conocer como crear una aplicación
- Conocer y definir una ruta en Django
- Conocer y definir una vista asociada a la ruta

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-03/Ejemplo-02`
1. Activar el entorno virtual __Bedutravels__

#### DESARROLLO
1. Crear el proyecto __Bedutravels__ con Django y cambiándonos a la carpeta del proyecto:

   ```console
   (Bedutravels) Ejemplo-02 $ django-admin startproject Bedutravels

   (Bedutravels) Ejemplo-02 $ tree Bedutravels
   Bedutravels
   ├── Bedutravels
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py

   (Bedutravels) Ejemplo-02 $ cd Bedutravels

   (Bedutravels) Ejemplo-02/Bedutravels $
   ```
   ***

1. Crear la aplicación __tours__ con el comando:

   ```console
   (Bedutravels) Ejemplo-02/Bedutravels $ python manage.py startapp tours

   (Bedutravels) Ejemplo-02/Bedutravels $ tree
   .
   ├── Bedutravels
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── tours
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

1. Ejecutar el proyecto __Bedutravels__ con:

   ```console
   Ejemplo-02/Bedutravels $ python manage.py runserver
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).

   You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.

   June 19, 2019 - 10:38:22
   Django version 2.2.2, using settings 'Bedutravels.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.   
   ```
   Si se abre la url indicada, se observará lo mismo que el "hola mundo!", así que sigamos un poco más adelante, nuestro objetivo es mostrar la página `index.html` pero como parte de la aplicación web.

   __Nota:__ Como el servidor bloquea la terminal, vamos a dejar esta terminal aquí y para los siguiente comandos abrir otra terminal, activar el entorno virtual Bedutravels y cambiarse a la carpeta de trabajo `Sesion-03/Ejemplo-02/Bedutravels/`.

1. Agrega la aplicación __tours__ a la configuración en el archivo `Bedutravels/Bedutravels/settings.py`:

   ```python
   # Application definition

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'tours',
   ]   
   ```

   __Revisar el flujo de una petición HTTP para el caso de Django:__

   [Ver diapos]

1. Agrega información regional a la configuración en el archivo `Bedutravels/Bedutravels/settings.py`:

   ```python
   # Internationalization
   # https://docs.djangoproject.com/en/2.2/topics/i18n/

   LANGUAGE_CODE = 'es-MX'

   TIME_ZONE = 'America/Mexico_City'
   ```
   Esto permite que el administrador de django esté en español, además de que el tratamiento de horas y fechas serán referidas a la zona horaria de México.

1. Mapear la url `/` con las rutas generales del proyecto __Bedutravels__ hacia las rutas de la aplicación __tours__

   ```
   url / -> Bedutravels/Bedutravels/urls.py -> Bedutravels/tours/urls.py
   ```

   __En el archivo `Bedutravels/Bedutravels/urls.py` agregar lo siguiente:__

   ```python
   from django.contrib import admin
   from django.urls import path, include  # modificada

   urlpatterns = [
       path('', include("tours.urls")),  # agregada
       path('admin/', admin.site.urls),
   ]
   ```

   En la vetana donde se está ejecutando el proyecto __Bedutravels__ se puede observar el siguiente mensaje de error:

   ```console
   (Bedutravels) Ejemplo-02/Bedutravels $ python manage.py runserver
   [...]
   File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
   ModuleNotFoundError: No module named 'tours.urls'
   ```
   Lo que indica que nos falta crear el archivo `urls.py` dentro de la carpeta `Bedutravels/tours/`

1. Mapear la url `/` con las rutas de la aplicación __tours__

   ```
   url / -> Bedutravels/tours/urls.py -> Bedutravels/tours/views.py
   ```

   __Crear el archivo `Bedutravels/tours/urls.py` con el siguiente contenido:__

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

   __Reiniciar Django para observar el resultado:__

   ```console
   [...]
   File "/home/rctorr/repos/Curso-Python-Expert/Sesion-03/Ejemplo-02/Bedutravels/tours/urls.py", line 5, in <module>
     path('', views.index, name='index'),
   AttributeError: module 'tours.views' has no attribute 'index'
   ```
   Lo que indica que en el archivo `tours/views.py` no existe una función llamada `index`, así que toca agregar dicha función.

1. Agregar la función/vista `index` al archivo `Bedutravels/tours/views.py` con el siguiente contenido:

   ```python
   from django.http import HttpResponse
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       return HttpResponse("<h2>Soy la página de inicio! Soy el amor te tu vida!</h2>")
   ```

   __Nota: Si la aplicación Django no está iniciada, iniciarla en este momento y abrir la siguiente url en el navegador__

   http://127.0.0.1:8000

   __El resultado debería ser el siguiente:__

   ![Página de inicio Bedutravels](assets/bedutravels-index-01.png)
   ***
