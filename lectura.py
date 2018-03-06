#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import re
from libs.estructuras import Pila,Nodo

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        elif lista[0] in variables:
                valor = variables[lista[0]]
                pila.apilar(Nodo(valor[0]))
        elif lista[0]=="=":
            variable = pila.desapilar().valor
            variables[variable] = [evaluar(pila.desapilar())]

            if  verificar(variable)== True:
                print(variable+" = "+str(variables[variable][0]))
            else:
                print("Error de token en el nombre de la variable: " + variable)
                return 0

        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

def evaluar(arbol):
    try:
        if arbol.valor == "+":
            return evaluar(arbol.izq) + evaluar(arbol.der)
        if arbol.valor == "-":
            return evaluar(arbol.izq) - evaluar(arbol.der)
        if arbol.valor == "/":
            return evaluar(arbol.izq) / evaluar(arbol.der)
        if arbol.valor == "*":
            return evaluar(arbol.izq) * evaluar(arbol.der)
        return int(arbol.valor)
    except ValueError:
         print "Error en el nombre de la variable: " + arbol.valor
         return 0



if __name__ == "__main__":
    pila = Pila()



    print("leyendo")
    lista = [y.split(" ")  for y in [x[:-1] for x in open("Expreciones.txt","r")]]
    print(lista)

    for exp in lista:
        print exp
