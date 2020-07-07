#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

# Función de inicio para nuestra aplicación y siempre lleva los
# parámetros environ y start_response.
def info_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    # Construyendo la respuesta HTML
    html = """
    <html>
        <body>
            <h1>Python Info</h1>
            <hr />
            <ul>
            {info}
            </ul>
            <hr />
            <p>Hecho con Python / Hecho con <3</p>
        </body>
    </html>
    """
    # Generando la info y creando un str
    info = ["<li>{}: {}</li>".format(k, v) for k, v in environ.items()]
    info = "\n".join(info)

    # Agregando la info a la plantilla HTML
    html = html.format(info=info)
    # Convirtiendo todo a utf-8
    html = html.encode("utf-8")

    # Se regresa el contenido de la respuesta
    return [html]

if __name__ == "__main__":
    # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
    # será el encargado de llamar a la app vía WSGI
    port = 8000
    host = "localhost"
    with make_server(host, port, info_app) as httpd:
        print("Esuchando en {}:{}... [Presiona Control+C para terminar!]".format(host, port))
        print("\nAbre la siguiente url en tu navegador:\n\n\thttp://{}:{}\n".format(host, port))

        # Esuchando peticiones hasta que se mate el proceso
        httpd.serve_forever()
