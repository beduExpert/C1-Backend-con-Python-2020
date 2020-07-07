`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo-03
## Agregar la página de inicio ya maquetada a la aplicación web

### OBJETIVOS
- Conocer como agregar páginas ya maquetadas por medio de las plantillas con Django.
- Conocer como configurar y agregar los archivos estáticos en una aplicación web con Django.
- Contar con la página de inicio del proyecto Bedutravels disponible con Django.

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-03/Ejemplo-03/Bedutravels/`
1. Activar el entorno virtual __Bedutravels__
1. Página de inicio maquetada del proyecto __Bedutravels__

   ![index.html](assets/bedutravels-index-01.png)

#### DESARROLLO
1. Ejecutar el proyecto __Bedutravels__ con:

   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ python manage.py runserver
   [...]
   June 19, 2019 - 10:38:22
   Django version 2.2.2, using settings 'Bedutravels.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.   
   ```
   ***

1. Haciendo uso de las plantillas de Django integrar la página de inicio maquetada que se encuentra en `public_html/index.html`.

   __Crear las carpetas `Bedutravels/tours/templates/tours`:__

   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ mkdir tours/templates
   (Bedutravels) Ejemplo-03/Bedutravels $ mkdir tours/templates/tours
   ```

   __Copiar el archivo `public_html/index.html` dentro de la carpeta `Bedutravels/tours/templates/tours/`:__

   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ cp ../public_html/index.html tours/templates/tours/

   (Bedutravels) Ejemplo-03/Bedutravels $ tree tours/templates/
   tours/templates/
   └── tours
       └── index.html
   ```

   __Modificar la función `index()` en el archivo `tours/views.py` para hacer uso de las plantillas (templates)__

   ```python
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       return render(request, "tours/index.html")
   ```
   Por omisión, Django busca los archivos html en la carpeta `proyecto/aplicacion/templates/aplicacion/`

   __El resultado en el navegador debería de ser el siguiente:__

   ![index.html con plantillas](assets/bedutravels-index-02.png)

   Hasta aquí ya podemos ver el html, pero ¿y los estilos y las imágenes?

   Como son archivos estáticos aún no hemos autorizado a que se puedan ver, así que continuemos.
   ***

1. Agregando acceso a los archivos estáticos (ruta y vista)

   __Crear la carpeta `Bedutravels/tours/static/tours/`:__

   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ mkdir tours/static
   (Bedutravels) Ejemplo-03/Bedutravels $ mkdir tours/static/tours
   ```

   __Copiar las carpetas de los archivos estáticos (css y img):__

   ```console
   (Bedutravels) Ejemplo-03/Bedutravels $ cp -a ../public_html/css tours/static/tours/

   (Bedutravels) Ejemplo-03/Bedutravels $ cp -a ../public_html/img tours/static/tours/

   Sesion-03/Ejemplo-03/Bedutravels $ tree -d 1 tours/static/tours/
   tours/static/tours/
   ├── css
   └── img
   ```

   __Finalmente hay que modificar la ruta en el archivo `index.html` para que usen el sistema de Django__

   Todas las url relativas o absolutas ahora tienen que ser absolutas e iniciar con `/static/tours/`, un ejemplos se muestra a continuación:

   ```html
   <!-- Animate.css -->
   <link rel="stylesheet" href="/static/tours/css/index.css">
   <!-- Icomoon Icon Fonts-->
   <link rel="stylesheet" href="/static/tours/css/destinos.css">
   ```
   Remplazar todas las coincidencias.

   __Actualizar el navegador y entonces se debería de ver la página mostrada al inicio__

   Si no funciona:
   - Recargar la página forzado actualizar el cache del navegador con `Control+Shift+R`.
   - En la ventana donde se está ejecutando el proyecto, deternlo y volver a iniciarlo.
   - Usar una ventana de incógnito.
   - Pedir ayuda a un experto (que no lo vas a encontrar en clase!)

   Si si funciona entonces:
   - Misión cumplida!
