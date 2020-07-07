#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import obtiene_viajes
from stdout import imprime_registros, imprime_registros_html

@click.command()
@click.option("--html", is_flag=True, help="Imprime la lista en formato HTML")
def lista_viajes(html):
    """
    Imprime la lista de viajes resercados en la salida estándar
    """
    # Se obtiene la lista de viajes
    viajes = obtiene_viajes()
    if html:
        # Se imprimen los viajes en formato html en la salida estándar
        imprime_registros_html(viajes, "Lista de viajes reservados")
    else:
        # Se imprimen los viajes en formato texto en la salida estándar
        imprime_registros(viajes, "Lista de viajes reservados")

if __name__ == '__main__':
    lista_viajes()
