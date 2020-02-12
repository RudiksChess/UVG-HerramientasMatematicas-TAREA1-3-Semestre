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
    Output: Resultado válido o inválido de ISBN10 basado en módulo 11 """

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
    Output: Resultado válido o inválido de ISBN13 basado en módulo 13 """


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

""" Función 5
    Input: un número de UPC sin verificador dando por el usuario 
    Output: Resultado UPC con verificador """

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

""" Función 6
    Input: un número de ISBN10 sin verificador dando por el usuario 
    Output: Resultado ISBN10 con verificador """

def ISBN10_Digito(numero):

    suma=0
    conversion= np.array(list(numero))

    for i,j in zip(conversion, reversed(range(2,11))):

        k = int(i)*j

        suma += k

    comprobacion = suma%11
    verificacion= (11-comprobacion)%11

    if isinstance(verificacion,int):
        print("---> El ISBN10 con el dígito identificador es:"+ numero+str(verificacion))

    else:
        print("---> Es un valor inválido de ISBN10\n")

""" Función 7
    Input: un número de ISBN13 sin verificador dando por el usuario 
    Output: Resultado ISBN13 con verificador """


def ISBN13_Digito(numero):

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
    verificador = 10-resultado

    if isinstance(verificador,int):
        print("---> El ISBN13 con el dígito identificador es:"+ numero+str(verificador))

    else:
        print("---> Es un valor inválido de ISBN 13\n")


""" Función 8
    Input: un número de NIT sin verificador dando por el usuario 
    Output: Resultado NIT con verificador """

def NIT_Digito(numero):

    st= numero[:-1]

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


    if isinstance(operacion5,int):
        print("---> El NIT con el digito identificador es: "+st+str(operacion5))

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

                 nit = str(input("Ingresar número de NIT: "))
                 nit2 = int(nit)

                 if isinstance(nit2,int):
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
              nit = str(input("Ingresar número de UPC sin verificador: "))
              UPC_Digito(nit)

          elif y ==2:
              isbn10_digito = str(input("Ingresar número de ISBN10 sin verificador: "))
              ISBN10_Digito(isbn10_digito)
          elif y ==3:
              isbn13_digito = str(input("Ingresar número de ISBN13 sin verificador: "))
              ISBN13_Digito(isbn13_digito)
          elif y ==4:
              nitdi = str(input("Ingresar número de NIT sin verificador: "))
              NIT_Digito(nitdi+"0")
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