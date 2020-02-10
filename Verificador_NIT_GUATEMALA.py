""" Función 4
    Input: un número de NIT dando por el usuario 
    Output: Resultado válido o inválido de NIT basado en una operación de la SAT """

import numpy as np 
import math
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

