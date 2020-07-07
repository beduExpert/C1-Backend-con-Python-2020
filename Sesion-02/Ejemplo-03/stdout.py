#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar imprimir información a la salida estándar (STDOUT)
"""

def imprime_registros(registros, titulo=None):
    """
    Imprime la lista de registros en la salida estándar en formato texto, cada
    registro es de tipo lista.

    titulo - Es de tipo str y si es proporcionado se imprime como título
    """
    # Se calcula el ancho máximo para cada columna
    anchos = [[len(str(campo)) for campo in reg] for reg in registros]
    anchos = [max(col) for col in zip(*anchos)]

    # Se imprime la lista
    print()
    if titulo: print(titulo)
    print("-" * len(titulo))
    for reg in registros:
        # Se formatea cada registro en una línea de texto
        reg = zip(reg, anchos)
        reg = ["{:{}}".format(*campo) for campo in reg]
        print(" | ".join(reg))
    print("-" * len(titulo))
    print()
