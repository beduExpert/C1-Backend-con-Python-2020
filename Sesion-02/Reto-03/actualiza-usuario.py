#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import actualiza_registro


@click.command()
@click.argument("id", type=int)
@click.argument("nombre")
@click.argument("apellidos")
@click.argument("edad")
@click.argument("genero")
def actualiza_usuario(id, nombre, apellidos, edad, genero):
    """
    Modifica un egistro de la tabla Usuario con los campos ID, NOMBRE,
    APELLIDOS, EDAD y GENERO. Si se proporciona un valor a un campo, ese
    valor será actualizado en la base de datos. Si no se desea actualizar
    un campo, entonces colocar el valor None.  Imprime un mensaje si el
    registro se atualiza exitosamente.
    """
    valor = lambda cad, valor: valor if cad == "None" else cad
    tabla = "Usuario"
    edad = valor(edad, None)
    try:
        registro = (
            valor(nombre, None),
            valor(apellidos, None),
            edad if edad == None else int(edad),
            valor(genero, None))
    except ValueError:
        print("\nError: La edad tiene que ser un valor entero\n")
        return
    if actualiza_registro(tabla, id, registro):
        registro = (id,) + registro
        print("Se ha actualizado el registro {} a la tabla {}".format(
            registro, tabla))

if __name__ == '__main__':
    actualiza_usuario()
