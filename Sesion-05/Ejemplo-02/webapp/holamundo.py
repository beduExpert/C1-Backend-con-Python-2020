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
            <p>Hola mundo y en español!</p>
        </body>
    </html>
    """.encode("utf-8")]

if __name__ == "__main__":
    # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
    # será el encargado de llamar a la app vía WSGI
    port = 8000
    host = "localhost"
    with make_server(host, port, hola_mundo_app) as httpd:
        print("Esuchando en {}:{}... [Presiona Control+C para terminar!]".format(host, port))
        print("\nAbre la siguiente url en tu navegador:\n\n\thttp://{}:{}\n".format(host, port))

        # Esuchando peticiones hasta que se mate el proceso
        httpd.serve_forever()
