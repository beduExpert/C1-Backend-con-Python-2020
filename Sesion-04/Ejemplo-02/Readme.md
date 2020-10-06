[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Ejemplo-02
## Definiendo y agregando autenticación de entrada usando la vista auth_views.login de Django.

### OBJETIVO
- Crear autenticación de entrada usando la vista auth_views.login de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Ejemplo-02`

### DESARROLLO
1. Modificar la ruta `/login` para hacer uso de la vista de Django

   __Se modifica el archivo `Bedutravels/tours/urls.py` con los siguientes imports:__
   ```python
   from django.contrib.auth import views as auth_views
   ```

   __Se modifica la ruta:__
   ```python
   path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
   ```
   Notar que se usa la misma plantilla login.html que ya se tenía, pero lo más importante es que no se necesita crear en este caso una vista, incluso se puede borrar la vista `login_user()`.

   __Borra la vista `login_user() del archivos views.py`__

   Verifica que el proceso de login y logout sigue funcionando, sin embargo se observa un error indicando que la página no ha sido encontrada, pero más aún observar la url que es `localhost:8000/accounts/profiles/`.

   Esta ruta es la que utiliza las vistas de Django por omisión, así que para indicar algo diferente se tiene que agregar un campo de entrada oculto en nuestra plantilla `index.html` de la siguiente forma:

   ```html
   <form class="profile-inputs" method="post">
         {% csrf_token %}
         Usuario: <input type="text" name="username" value="" required>
         Clave: <input type="password" name="password" value="" required>
         <!-- Para indicar a que url se redirige después de hacer login -->
         {% if next %}
         <input type="hidden" name="next" value="{{ next }}" />
         {% else %}
         <input type="hidden" name="next" value="/" />
         {% endif %}
         <button class="button-tour margin-top-sm" style="align-self: center; width:50%;" type="submit" name="button">
           Entrar
         </button>
   </form>
   ```
   Observar que el campo se llama `next` y después de hacer login, si no se indica otro valor, se redirecionará a la página principal.

   Ahora si, ya puedes hacer login y deberías de ver la lista de tours disponibles.

Esto está bien si no se necesita personalizar el proceso de login, de lo contrario si es necesario crear el proceso a mano.
