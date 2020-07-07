#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import obtiene_registros, obtiene_tablas
from stdout import imprime_registros

@click.command()
@click.argument("tabla", required=False)
def lista_registros(tabla):
    """
    Imprime la lista de registros de TABLA  en la salida estándar, si no se
    proporciona una tabla, se imprime la Lista de tablas disponibles.
    """
    if tabla:
        # Se obtiene la lista de registros de tabla
        registros = obtiene_registros(tabla)
        # Se imprimen los registros en formato texto en la salida estándar
        imprime_registros(registros, "Tabla: {}".format(tabla))
    else:
        tablas = obtiene_tablas()
        imprime_registros(tablas, "Tablas disponibles")

if __name__ == '__main__':
    lista_registros()
