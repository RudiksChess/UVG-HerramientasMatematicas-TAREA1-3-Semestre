""" Función 4
    Input: un número de NIT dando por el usuario 
    Output: Resultado válido o inválido de NIT basado en una operación de la SAT """

import numpy as np 
import math



def UPC_Digito(num):

    impares = 0
    pares = 0
    for i, lol in enumerate(num):
        j = i+1

        if j % 2 == 0:
            pares += int(lol)
        else:
            impares += int(lol)

    suma = (impares * 3) + pares

    resultado = suma % 10

    digito = 10- resultado

    if digito == 10:
        digito == 0


    numfinal = num+ str(digito)
    numfinalint = int(numfinal)

    if isinstance(numfinalint,int):
        print("---> El NIT con el digito identificador es: "+numfinal)

    else:
        print("---> Es un valor inválido de UPC\n")


vat = "04210000526"

UPC_Digito(vat)