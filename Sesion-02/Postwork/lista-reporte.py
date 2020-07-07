#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import obtiene_reporte
from stdout import imprime_registros, imprime_registros_html

@click.command()
@click.option("--html", is_flag=True, help="Imprime la lista en formato HTML")
def lista_reporte(html):
    """
    Imprime el reporte en la salida estándar
    """
    # Se obtiene la lista registros para el reporte
    registros = obtiene_reporte()
    if html:
        # Se el reporte en formato html en la salida estándar
        imprime_registros_html(registros, "Reporte fulanito")
    else:
        # Se imprimen el reporte en formato texto en la salida estándar
        imprime_registros(registros, "Reporte fulanito")

if __name__ == '__main__':
    lista_reporte()
