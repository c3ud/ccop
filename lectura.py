#!/usr/local/bin/python
# -*- coding: utf-8 -*-

## listas por comprension


print("leyendo")
lista = [y.split(" ")  for y in [x.strip("=\n") for x in open("operacion.txt","r")]]
print("Datos Almacenados")
print(lista)

charAcepted = "1234567890+-*/"

for x in lista:
    for y in x:
        if y not in charAcepted:
            print type(y)
            print( y + " : is not accepted")
