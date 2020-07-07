#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from wsgiref.util import FileWrapper
from wsgiref.simple_server import make_server

# Carpeta donde se encuentras las imágenes
DIR_IMG = "img"

# Función de inicio para nuestra aplicación y siempre lleva los
# parámetros environ y start_response.
def imagen_app(environ, start_response):
    """ Función encargada de responder a todas las peticiones """
    # Obtenemos la lista de la imágenes
    imagenes = os.listdir(DIR_IMG)

    # Obtener el nombre de la imagen que el usuario quiere visualizar
    nomimg = environ["PATH_INFO"].replace("/", "")

    # Está la imagen solicitada por el usuario en nuestra lista?
    if nomimg in imagenes:
        # Si si, entonces le regreamos la imagen con OK y tipo incluído
        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'image/png')]
        start_response(status, headers)

        # Juntamos el nombre de la imagen con el directorio
        pathimg = os.path.join(DIR_IMG, nomimg)
        # Regresamos en la imagen como un conjunto de bytes, notar el
        # "rb". FileWrapper es el equivalente a os.write
        return FileWrapper(open(pathimg, "rb"))
    else:
        # S no, entonces enviamos un error al usuario indicando que la
        # imagen solicitada no existe.
        status = '401 Error'  # HTTP Status
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)

        # Recordar que siempre hay que regresar Bytes y no str
        return ["<h2>Error: ruta incorrecta!</h2>".encode("utf-8")]

if __name__ == "__main__":
    # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
    # será el encargado de llamar a la app vía WSGI
    port = 8000
    host = "localhost"
    with make_server(host, port, imagen_app) as httpd:
        print("Esuchando en {}:{}... [Presiona Control+C para terminar!]".format(host, port))
        print("""
Abre la siguiente url en tu navegador:

    http://{}:{}/python-logo.png
        """.format(host, port))

        # Esuchando peticiones hasta que se mate el proceso
        httpd.serve_forever()
