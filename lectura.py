#!/usr/local/bin/python
# -*- coding: utf-8 -*-

## listas por comprension


print("leyendo")
lista = [y.split(" ")  for y in [x.strip("=\n") for x in open("operacion.txt","r")]]
print(lista)
