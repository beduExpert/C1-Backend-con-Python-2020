`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Ejemplo-02
## Conociendo la interface WSGI por medio de la aplicación web "hola mundo" con Python.

### OBJETIVO
Comprender el flujo de información entre un servidor web y una aplicación en Python por medio de la interface WSGI (Web Server Gateway Interface).

#### REQUISITOS
1. Actualizar repositorio
1. Revisar diagrama del flujo de la interface WSGI [Ver diapo.]
1. La interface WSGI es un estándar y su especificación puede ser encontrada en:
   - https://www.python.org/dev/peps/pep-3333/
   - https://wsgi.readthedocs.io/en/latest/index.html
   - http://wsgi.tutorial.codepoint.net/
1. Usar el módulo __wsgiref__ que es parte de la librería estándar de Python y su documentación está en:
   - https://docs.python.org/3.7/library/wsgiref.html

#### DESARROLLO
1. Entendiendo la interface WSGI: Creando la aplicación web en la carpeta `webapp/` con el nombre `holamundo.py` con el siguiente contenido:

    ```python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from wsgiref.simple_server import make_server

    # Función de inicio para nuestra aplicación y siempre lleva los
    # parámetros environ y start_response.
    def hola_mundo_app(environ, start_response):
        status = '200 OK'  # HTTP Status
        # HTTP Headers a incluir en la respuesta
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        # Se regresa el contenido de la respuesta
        return ["""
        <html>
            <body>
                <h1>Hecho con Python</h1>
                <h3>Hecho con <3</h3>
                <hr />
                <p>Hola mundo!</p>
            </body>
        </html>
        """]

    if __name__ == "__main__":
        # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
        # será el encargado de llamar a la app vía WSGI
        port = 8000
        host = "localhost"
        with make_server(host, port, hola_mundo_app) as httpd:
            print("Esuchando en {}:{}... [Presiona Ctrol+C para terminar!]".format(host, port))

            # Esuchando peticiones hasta que se mate el proceso
            httpd.serve_forever()    
    ```

1. Entendiendo la interface WSGI: Iniciando un micro servidor web con Python

   __Cambiarse a la carpeta `webapp`:__
   ```console
   Sesion-02/Ejemplo-02 $ cd webapp
   Sesion-02/Ejemplo-02/webapp $
   ```

   __Crear el servidor con la instrucción:__
   ```console
   Sesion-02/Ejemplo-02/webapp $ python holamundo.py
   Esuchando en localhost:8000... [Presiona Ctrol+C para terminar!]
   ```
   El servidor se inicia en todas las ¿interfaces? del equipo en el puerto 8000 quedando en espera de peticiones hasta que se presione Control+C.

   Se puede acceder abriendo la siguiente url en algún navegador:
   - http://localhost:8000

1. Entendiendo la interface WSGI: Solicitando el archivo `python-logo.png`:

   El servidor web por medio de la interface WSGI lo que hace es mostrar sólamente la información que la webapp `holamundo.py` tiene definido y peticiones a otros archivos o aplicaciones no está permitido o como en esta caso, son simplemente ignoradas. Por ejemplo abrir la siguiente url en el navegador y comentar el resultado:
   - http://localhost:8000/python-logo.png

   Notar que el archivo `python-logo.png` se encuentra en la misma carpeta.
   ***
