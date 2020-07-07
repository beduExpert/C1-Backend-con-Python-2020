#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

with open("img/python-logo.png", "rb") as inpng:
    imagen = inpng.read()

# 1 es el descriptor de archivo a nivel S.O. para
# la salida estándar.
os.write(1, b"Content-Type: image/png\n\n")
os.write(1,imagen)
