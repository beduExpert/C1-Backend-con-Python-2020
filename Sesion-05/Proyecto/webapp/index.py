#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file, request

HOST = "localhost"
PORT = 8000

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

@route("/")
def index():
    # Obteniendo el archivo html para el formulario
    with open("formulario.html") as da:
        html = da.readlines()

    return html

@route("/", method="POST")
def action_index():
    # Obteniendo el archivo html para la respuesta
    with open("formulario_resp.html") as da:
        html = da.read()

    # Obteniendo los valores enviados por el formulario
    email = request.forms.get("email")
    clave = request.forms.get("clave")

    # Actualizando el html con los valores
    html = html.format(email=email, clave=clave)
    return html.split("\n")


if __name__ == "__main__":
    # Inicializa el servidor de la aplicación web
    run(host=HOST, port=PORT, debug=True, reloader=True)
