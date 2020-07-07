[`Backend con Python`](../../Readme.md) > [`Sesión 05`](../Readme.md) > Ejemplo-01
## Definiendo y agregando autenticación de entrada usando el modelo User de Django

### OBJETIVO
- Conocer el modelo User de Django
- Crear autenticación de entrada para una página de la aplicación

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Clase-10/Ejemplo-01`
1. Diagrama del modelo entidad-relación para el proyect __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](assets/bedutravels-modelo-er.jpg)

### DESARROLLO
1. Conociendo el modelo User de Django:

   __Iniciar el shell de Django:__
   ```console
   Ejemplo-01/Bedutravels $ python manage.py shell
   Python 3.7.3 (default, Mar 27 2019, 22:11:17)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>>
   ```

   __Listando los registros en el modelo User:__

   ```python
   >>> from django.contrib.auth.models import User
   >>> User.objects.all()
   <QuerySet [<User: bedutravels>]>
   >>> u1 = User.objects.get(pk=1)
   >>> u1.username
   'bedutravels'
   >>> u1.email
   'bedutravels@gmail.com'
   ```

   __Validando datos de usuario contra los datos del modelo User:__

   ```python
   >>> from django.contrib.auth import authenticate
   >>> username = "bedutravels"
   >>> password = "bedu"
   >>> authenticate(username=username, password=password)
   >>> acceso = authenticate(username=username, password=password)
   >>> print(acceso)
   None
   >>> acceso == None
   True
   >>> password = "bedutravels"
   >>> acceso = authenticate(username=username, password=password)
   >>> acceso
   <User: bedutravels>
   ```
   ***

1. Modificando la vista `login()` para incluir la validación usando el modelo User de Django.

   __Modificando los import para poder utilizar la funciones `authenticate` y `login`:__
   ```python
   from django.contrib.auth import authenticate, login
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import render, redirect
   from .models import User, Zona, Tour

   import datetime
   ```

   __Modificar la función login() de la sigiente manera:__
   ```python
   def login_user(request):
       """ Atiende las peticiones de GET /login/ """

       # Si hay datos vía POST se procesan
       if request.method == "POST":
           # Se obtienen los datos del formulario
           username = request.POST["username"]
           password = request.POST["password"]
           next = request.GET.get("next", "/")
           acceso = authenticate(username=username, password=password)
           if acceso is not None:
               # Se agregan datos al request para mantener activa la sesión
               login(request, acceso)
               # Y redireccionamos a next
               return redirect(next)
           else:
               # Usuario malo
               msg = "Datos incorrectos, intente de nuevo!"
       else:
           # Si no hay datos POST
           msg = ""
   [...]
   ```
   Como estamos importando la función `login()` de Django, tenemos que cambiar el nombre de nuestra función para que no entren en conflicto, así que la renombramos a `login_user()`.

   __Ahora como cambiamos el nombre de la vista, hay que actualizar la ruta en `urls.py`:__
   ```python
   path("login/", views.login_user, name="login_user"),
   ```

   __Se agrega el decorador a la vista que necesita ser autenticada:__
   ```python
   @login_required()
   def index(request):
       """ Vista para entender la petición de la url / """

       # Se obtiene la lista de todos los Tours y Zonas
       tours = Tour.objects.all()
       zonas = Zona.objects.all()
   [...]
   ```

   __Se le indica a Django que la url para el login es `/login/` agregando la siguientes líneas al archivos `Bedutravels/Bedutravels/settings.py`:__
   ```python
   # Se define la URL para login
   LOGIN_URL = "/login/"
   ```

   Ahora cada vez que se abra la url `/` si no se está registrado en el sistema, no se podrá entrar a ver la lista de tours.
   ***

1. Modificando el archivo `index.html` para indicar cuando hay usuario activo o no.

   __Realizar las siguientes modificaciones al archivo `Bedutravels/tours/templates/tours/index.html`:__
   ```html
   <nav class="menu_main">
       <a class="marca" href="#">
         <strong>BEDUTRAVELS</strong>
       </a>
       <div>
         <a href="#">{{ user.username }}</a>
         <a href="/logout/">Salir</a>
       </div>
   </nav>
   ```
   Las plantillas o archivos html siempre reciben la información del usuario actual activo.

__Felicidades!__ Otro éxito más, ya sólo falta un detalle así que mira el Reto-02 para resolverlo.
