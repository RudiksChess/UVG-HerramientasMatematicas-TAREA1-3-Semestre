"""
Created on Wed Feb  5 08:29:58 2020

@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas
"""
import numpy as np
import math

""" Función 1
    Input: un número de UPC dando por el usuario 
    Output: Resultado válido o inválido de UPC basado en módulo 10 """

def UPC(numero):

    impares = 0
    pares = 0
    for i, lol in enumerate(numero):
        j = i+1

        if j % 2 == 0:
            pares += int(lol)
        else:
            impares += int(lol)

    suma = (impares * 3) + pares

    resultado = suma % 10

    if resultado ==0:
        print("---> Es un valor válido de UPC\n")

    else:
        print("---> Es un valor inválido de UPC\n")

""" Función 2
    Input: un número de ISBN10 dando por el usuario 
    Output: Resultado válido o inválido de UPC basado en módulo 11 """

def ISBN10(numero):
    suma=0
    conversion= np.array(list(numero))

    for i,j in zip(conversion, range(1,11)):

        k = int(i)*j

        suma += k

    comprobacion = suma%11

    if comprobacion == 0:
        print("---> Es un valor válido de ISBN10\n")

    else:
        print("---> Es un valor inválido de ISBN10\n")


""" Función 3
    Input: un número de ISBN13 dando por el usuario 
    Output: Resultado válido o inválido de UPC basado en módulo 13 """


def ISBN13(numero):

    impares = 0
    pares = 0
    for i, lol in enumerate(numero):
        j = i+1

        if j % 2 == 0:
            pares += int(lol)
        else:
            impares += int(lol)

    suma = (pares * 3) + impares

    resultado = suma % 10

    if resultado ==0:
        print("---> Es un valor válido de ISBN 13\n")

    else:
        print("---> Es un valor inválido de ISBN 13\n")

""" Función 4
    Input: un número de NIT dando por el usuario 
    Output: Resultado válido o inválido de NIT basado en una operación de la SAT """
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



lol = int(input("\n|BIENVENIDO AL VERFICADOR DE CÓDIGOS: | \n" +

            "SELECCIONE UNA OPCIÓN: \n\n" +
            "1. VERIFICAR \n" +
            "2. CREAR DÍGITO DE CONTROL\n" +
            "3. SALIR \n\n" +
            "OPCIÓN:"))

while lol !=3:

 try:

    if lol ==1:

        x = int(input("¿Qué código quiere comprobar?: \n" +
                          "1. UPC \n" +
                          "2. ISBN - 10 \n" +
                          "3. ISBN - 13 \n" +
                          "4. NIT \n" +
                          "5. Salir\n" +
                          " Opción:"))
        while x != 5:

             if x ==1:
                 upc = str(input("Ingresar número UPC: "))

                 if len(upc) ==12:
                     UPC(upc)


                 else:
                     print("No es un valor admitido de UPC, vuelva a intentarlo.")


             elif x ==2:
                 isbn10 = str(input("Ingresar número ISBN-10: "))

                 if len(isbn10) ==10:
                     ISBN10(isbn10)

                 else:
                     print("No es un valor admitido de ISBN-10, vuelva a intentarlo.")

             elif x ==3:
                 isbn13 = str(input("Ingresar número ISBN-13: "))

                 if len(isbn13) ==13:
                     ISBN13(isbn13)

                 else:
                     print("No es un valor admitido de ISBN-13, vuelva a intentarlo.")

             elif x ==4:
                 print("4")

                 nit = str(int(input("Ingresar número de NIT: ")))

                 if len(nit) ==12:
                     NIT(nit)

                 else:
                     print("No es un valor admitido de NIT, vuelva a intentarlo.")

             else:

                 print("Ingresar valor válido")

             x = int(input("¿Qué código quiere comprobar?: \n" +
                           "1. UPC \n" +
                           "2. ISBN - 10 \n" +
                           "3. ISBN - 13 \n" +
                           "4. NIT \n" +
                           "5. Salir\n" +
                           " Opción:"))



    elif lol ==2:

      y = int(input("¿A qué código quiere generarle un número de verificación?: \n" +
                    "1. UPC \n" +
                    "2. ISBN - 10 \n" +
                    "3. ISBN - 13 \n" +
                    "4. NIT \n" +
                    "5. Salir\n" +
                    " Opción:"))
      while y != 5:

          if y ==1:
              print("1")
          elif y ==2:
              print("2")
          elif y ==3:
              print("3")
          elif y ==4:
              print("4")
          else:

              print("Ingresar valor válido")

          y = int(input("¿A qué código quiere generarle un número de verificación?: \n" +
                        "1. UPC \n" +
                        "2. ISBN - 10 \n" +
                        "3. ISBN - 13 \n" +
                        "4. NIT \n" +
                        "5. Salir\n" +
                        " Opción:"))





    else:

        print("Vuelva a ingresar un valor válido")




    lol = int(input("\n|BIENVENIDO AL VERFICADOR DE CÓDIGOS: | \n" +

                "SELECCIONE UNA OPCIÓN: \n\n" +
                "1. VERIFICAR \n" +
                "2. DÍGITO DE CONTROL\n" +
                "3. SALIR \n\n" +
                "OPCIÓN:"))

 except ValueError:

     print("ERROR: Está ingresando un valor no númerico")