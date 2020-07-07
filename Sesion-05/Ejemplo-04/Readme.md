`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-04

## Introducción a los micro frameworks creando la micro aplicación "hola mundo" con Bottle.

### OBJETIVOS
- Conocer el concepto de framework para la creación de aplicaciones web por medio de Python.
- Conocer el flujo de información entre una petición de usuario y una aplicación web creada usando el micro framework Bottle.

#### REQUISITOS
1. Revisar el concepto de frameworks [Ver diapo]
1. Actualizar repositorio
1. Instalar el módulo Bottle (si has actualizado tus carpetas con el repo seguro ya lo tienes)

   __Bottle__ Es un micro framework que permite crear aplicaciones web monolíticas, es decir, donde muchos usuarios pueden consultar información, pero, sólo uno puede agregar o modificar la información.

   Sitio web: http://bottlepy.org/docs/dev/index.html

   Este módulo en particular se puede Instalar de dos formas, una es por medio del comando __pip__ y otra es obteniendo y copiando el archivo `bottle.py` a la carpeta donde se creará la aplicación, esto es gracias a que todo el framework de __Bottle__ vive en un sólo archivo.

#### DESARROLLO
1. Entendiendo a los frameworks: Creando la aplicación web `webapp/holamundo.py` con el siguiente contenido:

   ```python
   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   from bottle import route, run

   HOST = "localhost"
   PORT = 8000

   @route("/")
   def index():
       return """
       <html>
           <body>
               <h1>Hecho con Bottle</h1>
               <hr />
               <p>Hola mundo y en español!</p>
               <hr />
               <p>Hecho con <3</p>
           </body>
       </html>
       """

   if __name__ == "__main__":
       run(host=HOST, port=PORT, debug=True)
   ```

1. Para ejecutar la aplicación se realiza lo siguiente:

   __Cambiarse a la carpeta `webapp`:__
   ```console
   Sesion-02/Ejemplo-04 $ cd webapp
   Sesion-02/Ejemplo-04/webapp $
   ```

   __Ejecutando el script con:__

   ```console
   Sesion-02/Ejemplo-04/webapp $ python holamundo.py
   Bottle v0.13-dev server starting up (using WSGIRefServer())...
   Listening on http://localhost:8000/
   Hit Ctrl-C to quit.
   ```

   El servidor se inicia en localhost del equipo en el puerto 8000 quedando en espera de peticiones hasta que se presione Control+C.

   Se puede acceder abriendo la siguiente url en algún navegador:
   - http://localhost:8000

1. ¿Qué sucede si se abre la siguiente petición?

   - http://localhost:8000/python-logo.png
   ***
