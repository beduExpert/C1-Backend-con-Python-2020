#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import agrega_registro


@click.command()
@click.argument("campo1")
@click.argument("campo2")
@click.argument("campo3", type=int)
def agrega_nombretabla(campo1, campo2, campo3):
    """
    Agrega un nuevo registro a la tabla NombreTabla con los campos CAMPO1,
    CAMPO2, CAMPO3, etc. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    tabla = "NombreTabla"
    registro = (campo1, campo2, campo3, etc)
    if agrega_registro(tabla, registro):
        print("Se ha agregado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    agrega_nombretabla()
