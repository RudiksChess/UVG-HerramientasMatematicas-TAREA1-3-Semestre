"""
Created on Wed Feb  5 08:29:58 2020

@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas
"""
import math

import numpy as np

def NIT(numero):


    suma=0

    conversion= np.array(list(numero))
    reversa= np.flip(conversion)
    eliminar1= np.delete(reversa,0)


    for i,j in zip(eliminar1, range(2,len(numero)+1)):

        k = int(i)*j

        suma += k

    comprobacion = math.floor(suma/11)
    verificacion = comprobacion*11
    operacion1 = suma - verificacion
    operacion2= math.floor(operacion1/11)
    operacion3= operacion2*11
    operacion4 = operacion1-operacion3
    operacion5= 11-operacion4


    if operacion5== int(conversion[-1]):
       print("---> Es un valor válido de NIT\n")

    else:
       print("---> Es un valor inválido de NIT\n")




vat = "102237134"

NIT(vat)

