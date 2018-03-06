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

def verificar(variable):
    patronVariable = re.compile('^[a-z][a-zA-Z_$0-9]*$')
    patronValor = re.compile('^[-+]?[0-9]+$')
    patronOperador = re.compile('^[+]$|^[*]$|^[-]$|^[/]$|^[=]$')
    comprobacion = True

    for i in variable:
        if(patronVariable.match(i)):
            var.append(i)
            tokens["Variable"]=var
        elif(patronValor.match(i)):
            val.append(i)
            tokens["Valor"]=val
        elif(patronOperador.match(i)):
            op.append(i)
            tokens["Operador"]=op
        else:
            error.append(i)
            comprobacion = False
    return comprobacion

if __name__ == "__main__":
    pila = Pila()
    variables = {}
    tokens = {}
    var = []
    val = []
    op = []
    error = []

    archivo = open("Expreciones.txt", "r")
    for linea in archivo.readlines():
        print linea.strip("\n").split(" ")
    exp = linea.strip("\n").split(" ")

    if(verificar(exp)):
        convertir(exp,pila)
    else:
        print "Se han encontrado errores"
        print "Errores: ",error
    for t in tokens:
        print(t," : ",tokens[t])
    var = []
    val = []
    op = []
    error = []
