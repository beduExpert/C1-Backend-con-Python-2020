#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import agrega_registro


@click.command()
@click.argument("nombre")
@click.argument("apellidos")
@click.argument("edad", type=int)
@click.argument("genero")
def agrega_usuario(nombre, apellidos, edad, genero):
    """
    Agrega un nuevo registro a la tabla Usuario con los campos NOMBRE,
    APELLIDOS, EDAD y GENERO. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    tabla = "Usuario"
    registro = (nombre, apellidos, edad, genero)
    if agrega_registro(tabla, registro):
        print("Se ha agregado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    agrega_usuario()
