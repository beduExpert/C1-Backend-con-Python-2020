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
