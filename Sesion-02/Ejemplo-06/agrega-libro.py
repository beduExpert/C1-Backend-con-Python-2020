#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import agrega_registro


@click.command()
@click.argument("titulo")
@click.argument("editorial")
@click.argument("numpag", type=int)
@click.argument("autores")
def agrega_usuario(titulo, editorial, numpag, autores):
    """
    Agrega un nuevo registro a la tabla Libro con los campos TITULO,
    EDITORIAL, NUMPAG y AUTORES. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    tabla = "Libro"
    registro = (titulo, editorial, numpag, autores)
    if agrega_registro(tabla, registro):
        print("Se ha agregado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    agrega_usuario()
