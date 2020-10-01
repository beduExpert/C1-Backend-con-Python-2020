[`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a un Proyecto

### OBJETIVOS
- Crear las tablas de tu modelo relacional con el modelo de datos de Django
- Crear las relaciones entre tablas según corresponda con el modelo de datos de Django.
- Usar las consultas junto a las plantillas de Django para mostrar datos de forma dinámica.
- Agregar una página con formulario y procesar la información.

#### REQUISITOS
1. Constar con la carpeta del repo actualizada.
1. Usar la carpeta de trabajo `Sesion-03/Postwork/Proyecto/`.
1. Activar el entorno virtual para tú proyecto.
1. Página de inicio maquetada del tú proyecto en la carpeta `Sesion-03/Postwork/public_html/`.

### DESARROLLO
1. Usando el modelo entidad-relación, crear el modelo correspondiente a cada tabla.

   __Creando el modelo para la tabla Tabla1 agregando lo siguiente al archivo `Proyecto/miapp/models.py`:__

   ```python
   from django.db import models

   # Create your models here.
   class Tabla1(models.Model):
       """ Define la tabla Tabla1 """
       campo1 = models.???
       campo2 = models.???
       campoN = models.???
   ```

   __Antes de continuar, tenemos que indicar a Django algunas configuraciones locales en el archivo `settings.py`:__

   ```python
   # Internationalization
   # https://docs.djangoproject.com/en/2.2/topics/i18n/

   LANGUAGE_CODE = 'es-MX'
   TIME_ZONE = 'America/Mexico_City'
   ```

   La lista tanto de códigos de lenguaje como de zonas horarias se puede consultar en:
   - http://www.i18nguy.com/unicode/language-identifiers.html
   - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

   __Avisando a Django que hemos modificado el archivo `models.py`:__

   ```console
   (Proyecto) Postwork/Proyecto $ python manage.py makemigrations
   (Proyecto) Postwork/Proyecto $ python manage.py migrate
   (Proyecto) Postwork/Proyecto $
   ```

   __Django ya cuenta con un sistema CRUD para nuestros modelos y para activarlo es necesario agregar un Tabla1 administrador cuando menos:__

   ```console
   (Proyecto) Postwork/Proyecto $ python manage.py createsuperuser
   Nombre de Tabla1 (leave blank to use 'rctorr'): Proyecto
   Dirección de correo electrónico: proyecto@gmail.com
   Password:
   Password (again):
   La contraseña es muy similar a  nombre de Usuario.
   Bypass password validation and create user anyway? [y/N]: y
   Superuser created successfully.

   (Proyecto) Postwork/Proyecto $
   ```

   Abrir la url http://localhost:8000/admin y usar los siguientes datos para entrar:
   - Usuario: Proyecto
   - Clave: Proyecto
   - Email: proyecto@gmail.com

   __Agregando el siguiente código al archivo `Proyecto/miapp/admin.py`:__

   ```python
   from django.contrib import admin
   from .models import Tabla1

   # Register your models here.
   admin.site.register(Tabla1)
   ```

   Ahora ya se puede listar, agregar, actualizar o eliminar registros en la tabla Tabla1.
   ***

1. Usando el modelo entidad-relación, crear las tablas y sus relaciones.

   ```python
   class TablaN(models.Model):
       """ Define la tabla TablaN """
       tabla1 = models.ForeignKey(Tabla1, on_delete=models.CASCADE)
       campo1 = ???
       campon = ???

       def __str__(self):
           """ Se define la representación en str para TablaN """
           return ???
   ```

   __Avisando a Django que hemos modificado el archivo `models.py`:__

   ```console
   (Proyecto) Ejemplo-02/Proyecto $ python manage.py makemigrations
   (Proyecto) Ejemplo-02/Proyecto $ python manage.py migrate
   (Proyecto) Ejemplo-02/Proyecto $
   ```

   __Agregando la tabla TablaN al administrador de Django y definiendo los campos a mostrar:__

   ```python
   from .models import Tabla1, TablaN

   class TablaNAdmin(admin.ModelAdmin):
       # Se sobre escribe lo que hace __str__
       list_display = ("id", "tabla1", "campo1", "campon")
   admin.site.register(TablaN, TablaNAdmin)
   ```
   Abrir el navegador en la siguiente url ...

   Abrir la url http://localhost:8000/admin y usar los siguientes datos para entrar:
   - Usuario: Proyecto
   - Clave: Proyecto

   __Se deberá de ver los distintos modelos agregados y se deberá de poder agregar registros a cada tabla.__
   ***
-
1. Usando el __Shell de Django__ definir las consultas que serán usadas para obtener los datos dinámicos para cada una de las páginas que lo requieran.

   __Iniciando el Shell de Django:__
   ```console
   (Proyecto) Postwork/Proyecto $ python manage.py shell
   Python 3.7.3 (default, Mar 27 2019, 22:11:17)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>>
   ```

   __Realizando la consulta para obtener todos los registros de la tabla ???:__

   ```python
   >>> from miapp.models import ???
   >>> ???.objects.all()
   <QuerySet [<???: Yo, Robot>, <???: El fin de la eternidad>, <???: El arte de la guerra>]>
   >>>
   ```
   ***

1. Imprime los datos de la tabla ??? el registro con `id = 3`:

   __Dentro el Shell de Django:__

   ```python
   >>> l3 = ???.objects.get(pk=3)
   >>> l3
   <???: El arte de la guerra>
   ```
   ***
-
1. Convertir la plantilla `index.html` en una página base y la página para el index.

   __Realizar una copia del archivo `index.html` y llamarla `base.html`:__

   ```console
   Postwork/Proyecto $ cp miapp/template/miapp/index.html miapp/template/base.html

   Postwork/Proyecto $
   ```
   __Modificar el archivo `base.html` para que se vea similar a lo siguiente:__

   ```html
   ...
   <title>Proyecto - {% block title %}título de página{% endblock %}</title>
   ...
       {% block contenido %}
       {% endblock %}
   ```

   __Ahora se modifica el archivo `index.html` para que se va de la siguiente forma:__

   ```html
   {% extends "base.html" %}
   ```

1. A partir de aquí crear las páginas restantes del proyecto siguiendo los siguientes puntos:

   - Agregar la ruta a la página en el archivo `urls.py`
   - Agregar la vista a la ruta en el archivo `views.py`
   - Agregar el archivos html que haga uso de base.html y que muestra el html de la página que se está agregando.
   - Agregar a la vista el código correspondiente a los datos o procesamiento POST necesario para la página en turno.
   ***

__Que Django te acompañe!__
