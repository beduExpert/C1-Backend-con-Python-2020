`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-01
## Conociendo el protocolo HTTP por medio de una micro aplicación Python

### OBJETIVO
Conociendo el flujo de información en una comunicación usando el protocolo HTTP entre un Navegador como cliente y una micro aplicación Python.

#### REQUISITOS
1. Actualizar repositorio
1. Revisar diagrama del flujo de una petición web [Ver diapo.]

#### DESARROLLO
1. Entendiendo el protocolo HTTP: Iniciando un micro servidor web con Python

   Se puede iniciar un servidor web usando el módulo `http` que es parte de la librería estándar y su documentación se puede consultar en https://docs.python.org/3.6/library/http.server.html

   __Cambiarse a la carpeta `html` del `Ejemplo-01`:__
   ```console
   Sesion-02/Ejemplo-01 $ cd html
   Sesion-02/Ejemplo-01/html $
   ```

   __Crear el servidor con la instrucción:__
   ```console
   Sesion-02/Ejemplo-01/html $ python -m http.server
   Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
   ```
   El servidor se inicia en todas las ¿interfaces? del equipo en el puerto 8000 quedando en espera de peticiones hasta que se presiones Control+C. Se sugiere dejar el servidor corriendo hasta nuevo aviso.

   Se puede acceder usando alguna de las siguiente formas:
   - http://localhost:8000
   - http://ip-address:8000

   El servidor lo que hace es mostrar los archivos contenidos en la carpeta donde fué ejecutado o en alguna de las carpetas de nivel inferior.
   ***

1. Entendiendo el protocolo HTTP: El encabezado `Content-type`.

   __Obtener el MIMEType de los siguientes archivos:__
   - Abrir el archivo `index-1.html` por medio del navegador y encontrar el MIMEType (Multipurpose Internet Mail Extension Type) usando las herramientas de desarrollo del navegador.
   - Abrir el archivo `python-logo.png` y encontrar el MIMEType
   - Arbrir el archivo `index.css` y encontrar el MIMEType

   El MIMEType es un estándar que indica el tipo de archivo que es abierto por los navegadores y hay una lista definida de los valores soportados y se puede consultar con mayor detalle en:

   [Developer Mozilla MIME_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)

   Además observar que a pesar de que el archivo `index.css` contiene código HTML, no se procesa como tal ya que la extensión del archivo `.css` predomina y se procesa como archivo de estilos.
   ***

1. Ejecutando código en Python llamado desde el navegador

   Una manera de ejecutar código en Python u otros lenguajes es haciendo uso de la interface CGI (Common Gateway Interfece).

   __Reiniciar el servidor http con la opción --cgi__

   En la terminal donde se está ejecutando el servidor presionar Control+C y ejecutar de nuevo el servidor de la siguiente forma:

   ```console
   Sesion-02/Ejemplo-01/html $ python -m http.server --cgi
   Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
   ```

   __Abrir el script en Python index.py__

   Para abrir el script acceder a la siguiente dirección desde el navegador:

   http://localhost:8000/cgi-bin/index.py

   Observar que el MIMEType no está definido, pero los navegadores hacer lo posible por determinarlo, en este caso muy posiblemente si se vea el HTML resultante, dependerá de las capacidades del navegador.

   __Pero podemos engañar al navegador:__

   Agrega las siguientes líneas al archivo `cgi-bin/index.py` justo antes del `print`:

   ```python
   print("Content-type: text/javascript")
   print()
   ```
   Actualizar la página en el navegador... ¿describe lo sucedido?

   Ahora modifica el texto `text/javascript` por `text/html` y describe el resultado.

#### AVERTENCIA
Aunque el uso de aplicaciones Python por medio de la interface CGI es posible hoy en día en muchos servidores, es una práctica poco recomendada debido a __no poder garantizar un nivel de seguridad__ ya que sería muy semejante a realizar aplicaciones con __PHP__, sin embargo en un proceso de migración de PHP a Python el uso de Python vía CGI podría ser una alternativa.
