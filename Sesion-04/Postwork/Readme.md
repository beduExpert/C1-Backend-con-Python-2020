[`Backend con Python`](../../Readme.md) > [`Sesión 05`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a tú Postwork.

### OBJETIVO
- Crear autenticación de entrada y salida para una página de la aplicación
- Crear la ruta y vista para eliminar un registro de uno o más modelos.
- Definir permisos en base a grupos para la eliminación de registros.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Postwork`
1. Contar con tú Proyecto ya en Django mostrando página de inicio con lista de registros cuando menos.
1. Contar con el maquetado del la página de `login.html`

### DESARROLLO
1. Agrega autetenticación de entrada a tú Proyecto
   - Modifica el archivo `login.html` para hacer uso de los nombres `username`  y `password` para los campos input y que además haga uso del archivo `base.html`.
   - Colocar el archivo `login.html` en la carpeta `Proyecto/miapp/templates/registration/`
   - Agregar la ruta `/login/` que haga uso de la vista `views.login` (versión personalizada) o `auth_views_LoginView` (versión ya incluida en Django).
   - Si has elegido la versión personalizada, entonces agregar la vista o función `login()` al archivo `Proyecto/myapp/views.py`.
   - Actualizar el archivo `settings.py` para actualizar la url por omisión para la ruta de `/login/`
   - Usar el decorador `@login_required()` en cada vista que necesite de un usuario validado para poder continuar.
   - Modifica el archivo `index.html` para incluir la opción de __Login__ en tu menú o dónde hayas elegido agregarlo y que hará uso de la url `/login/`
   ***

1. Comprueba los siguiente casos para la autenticación de entrada
   - Al dar click en la opción de __Login__ se muestre la página de `login.html`
      - Que al proporcionar los datos incorrectos se regrese a la página de login mostrando un mensaje de que los datos son incorrectos.
      - Si los datos proporcionados son correcto, entonces se debe redireccionar a la página `index.html` o a la definida en la vista `login()`.
      - Se muestre el nombre del usuario en la barra de menú o en la sección indicada para ello.
   - Al dar click en una opción de menú restringida, si no se ha entrado con un usuario, se debe mostrar la página de `login.html`
   ***

1. Agrega autetenticación de salida a tú Proyecto
   - Agregar la ruta `/logout/` que haga uso de la vista `views.logout` (versión personalizada) o `auth_views_LogoutView` (versión ya incluida en Django).
   - Si has elegido la versión personalizada, entonces agregar la vista o función `logout()` al archivo `Proyecto/myapp/views.py`.
   - Modifica el archivo `base.html` para incluir la url `/logout/` en el nombre del usuario o en alguna opción de __Salir__ que se haya definido.
   - Validar que al dar click en el nombre de usuario ocurra lo siguiente:
      - En la barra de menú el nombre del usuario, cambia a __Login__
      - Si se da click en una opción restringida deberá aparecer la página `login.html` para poder continuar.
   ***

1. Agregar acciones en base a permisos por grupos
   - Si en tu proyecto existe una o más acciones que sólo cierto grupo de usuarios pueden realizar, entonces define los grupos que sean necesario y crealos usando el administrador de Django.
   - En la páginas donde se necesiten mostrar las acciones agrega el código html, css y javascript necesario para que las acciones se muestren en las páginas, asigna una url a cada acción (ej. `/cuento/eliminar/id/`, `/plantilla/texto/agregar/`)
   - Crea las rutas y vistas para atender las url's definidas
   - Ahora tanto en las los archivos html como en las vistas correspondiente en el archivo `views.py` agrega el código necesario para mostrar o realizar la acción sólo si el usuario pertenece al grupo autorizado, en caso contrario las opciones no se muestran o no se realizan.
   - Validar lo siguiente:
      - Con un usuario activo que no pertenece al grupo privilegiado entrar a la página con las acciones restringidas, no se deberán mostrar.
      - Desde el administrador de Django agregar el grupo al usuario activo, actualizar la página y ahora se debería de observar las acciones restringidas.
