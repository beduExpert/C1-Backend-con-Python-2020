#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar las operaciones a la base de datos MariaDB
"""

# Datos de conexión a la base de datos
BD = {
    "database":"Banco",
    "host":"localhost",
    "user":"Banco",
    "password":"Banco"
}

# zona de imports
from mysql.connector import connect, Error


def conecta_bd():
    """
    Se conecta a la base de datos BD, regresa un conecto o None en caso
    de error.
    """
    try:
        conn = connect(**BD)
    except Error as err:
        print(err)
        return None

    return conn

def obtiene_registros(tabla):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {}".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registros = [[r[0].capitalize() for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registros += cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def obtiene_tablas():
    """
    Obtiene la lista de tablas en la base de datos
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SHOW TABLES"
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de resultados de la consulta SQL
        registros = cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def agrega_registro(tabla, valores):
    """ Agrega un registro en tabla """
    # Se realiza la conexión a la BD
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos símbolos "%s" como valores
        # tengamos separados por comas
        signos = ", ".join(["%s"] * len(valores))
        # Se crea la consulta en SQL
        sql = "insert into {} values (null, {})".format(tabla, signos)
        # Se ejecuta la consulta
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()
        # Se cierra la BD
        conn.close()
        # Se regresa True para indicar que el registro se ha insertado con
        # éxito
        return True

    return False  # En caso de error

def obtiene_registro(tabla, id):
    """
    Obtiene el registro id de tabla
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {} WHERE id=%s".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql, (id,))
        # Se obtiene el resultados de la consulta SQL
        registro = cur.fetchone()
        # Se cierra la BD
        conn.close()

        return registro
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return None

def actualiza_registro(tabla, id, valores):
    """ Modifica un registro de la tabla """
    # Se realiza la conexión a la BD
    conn = conecta_bd()
    if conn:
        valores = (id,) + valores
        registro = obtiene_registro(tabla, id)
        registro = [t[0] if t[1] == None else t[1]
            for t in zip(registro, valores)]
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos símbolos "%s" como valores
        # tengamos separados por comas
        signos = ", ".join(["%s"] * len(valores))
        # Se crea la consulta en SQL
        sql = "REPLACE INTO {} VALUES ({})".format(tabla, signos)
        # Se ejecuta la consulta
        cur.execute(sql, registro)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()
        # Se cierra la BD
        conn.close()
        # Se regresa True para indicar que el registro se ha insertado con
        # éxito
        return True

    return False  # En caso de error
