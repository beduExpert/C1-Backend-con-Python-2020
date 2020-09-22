`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Ejemplo-03
## Agregar la página de inicio ya maquetada a la aplicación web

### OBJETIVOS
- Conocer como agregar páginas ya maquetadas por medio de las plantillas con Django.
- Conocer como configurar y agregar los archivos estáticos en una aplicación web con Django.
- Contar con la página de inicio del proyecto Bedutravels disponible con Django.

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-01/Ejemplo-03/django/`
1. Activar el entorno virtual __django__
1. Página de inicio maquetada del proyecto __Banco__

   ![](img/1.png)

#### DESARROLLO
1. Ejecutar el proyecto __Banco__ con:

   ```console
   python3 manage.py runserver   
   ```
   
   ![](img/2.png)
   ***

1. Haciendo uso de las plantillas de Django integrar la página de inicio maquetada que se encuentra en `public_html/index.html`.

   __Crear las carpetas `Banco/tarjeta/templates/tarjeta`:__

   ```console
   $ mkdir tarjeta/templates
   $ mkdir tarjeta/templates/tarjeta
   ```

   __Copiar el archivo `public_html/index.html` dentro de la carpeta `Banco/tarjeta/templates/tarjeta/`:__

   ```console
   cp ../../public_html/index.html tarjeta/templates/tarjeta
   ```

   __Modificar la función `index()` en el archivo `tarjeta/views.py` para hacer uso de las plantillas (templates)__

   ```python
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       return render(request, "tarjeta/index.html")
   ```
   
   ![](img/3.png)
   
   Por omisión, Django busca los archivos html en la carpeta `proyecto/aplicacion/templates/aplicacion/`

   __El resultado en el navegador debería de ser el siguiente:__

   ![](img/4.png)

   Hasta aquí ya podemos ver el html, pero ¿y los estilos y las imágenes?

   Como son archivos estáticos aún no hemos autorizado a que se puedan ver, así que continuemos.
   ***

1. Agregando acceso a los archivos estáticos (ruta y vista)

   __Crear la carpeta `Banco/tarjeta/static/tarjeta/`:__

   ```console
   mkdir tarjeta/static
   mkdir tarjeta/static/tarjeta
   ```

   __Copiar las carpetas de los archivos estáticos (css y img):__

  ![](img/5.png)

   __Finalmente hay que modificar la ruta en el archivo `index.html` para que usen el sistema de Django__

   Todas las url relativas o absolutas ahora tienen que ser absolutas e iniciar con `/static/tarjeta/`, un ejemplos se muestra a continuación:

   ```html
   <!-- Animate.css -->
   <link rel="stylesheet" href="/static/tarjeta/css/index.css">
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

![](img/6.png)