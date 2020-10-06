[`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-01
## Definiendo y agregando autenticación de salida usando el modelo User de Django

### OBJETIVO
- Crear autenticación de salida para una página de la aplicación

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Reto-01`

### DESARROLLO
1. Agrega la ruta para la url `/logout/`

   __Se modifica el archivo `Bedutravels/tours/urls.py` con lo siguiente:__
   ```python
   path("logout/", views.logout_user, name="logout_user"),
   ```

1. Agrega la vista `views.logout_user` para la ruta `logout/`

   __Se modifica el archivo `Bedutravels/tours/views.py` con lo siguiente:__
   ```python
   def logout_user(request):
       """ Atiende las peticiones de GET /logout/ """
       # Se cierra la sesión del usuario actual
       logout(request)

       return redirect("/login/")
   ```

   __Se tiene que importar la función `logout()` de la siguiente forma:__
   ```python
   from django.contrib.auth import authenticate, login, logout
   ```
   Validar que mediante el menú se pueda entrar y salir del sistema.

Eso es todo, ya cuentas con un sistema con entrada y salida de usuarios.
