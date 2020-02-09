"""
Created on Wed Feb  5 08:29:58 2020

@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas
"""
import numpy as np

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







lol = int(input("\n|BIENVENIDO AL VERFICADOR DE CODIGOS: | \n" +

            "SELECCIONE UNA OPCION: \n\n" +
            "1. VERIFICAR \n" +
            "2. DIGITO DE CONTROL\n" +
            "3. SALIR \n\n" +
            "OPCION:"))

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
                 isbn10 = int(input("Ingresar número ISBN-10: "))

                 if len(isbn10) ==10:
                     print("1")

                 else:
                     print("No es un valor admitido de ISBN-10, vuelva a intentarlo.")

             elif x ==3:
                 isbn13 = int(input("Ingresar número ISBN-13: "))

                 if len(isbn13) ==13:
                     print("1")

                 else:
                     print("No es un valor admitido de ISBN-13, vuelva a intentarlo.")

             elif x ==4:
                 print("4")

                 isbn13 = int(input("Ingresar número de NIT: "))

                 if len(isbn13) ==12:
                     print("1")

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

      y = int(input("¿A 1ué código quiere generarle un número de verificación?: \n" +
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

          y = int(input("¿A 1ué código quiere generarle un número de verificación?: \n" +
                        "1. UPC \n" +
                        "2. ISBN - 10 \n" +
                        "3. ISBN - 13 \n" +
                        "4. NIT \n" +
                        "5. Salir\n" +
                        " Opción:"))





    else:

        print("Vuelva a ingresar un valor válido")




    lol = int(input("\n|BIENVENIDO AL VERFICADOR DE CODIGOS: | \n" +

                "SELECCIONE UNA OPCION: \n\n" +
                "1. VERIFICAR \n" +
                "2. DIGITO DE CONTROL\n" +
                "3. SALIR \n\n" +
                "OPCION:"))

 except ValueError:

     print("ERROR: Está ingresando un valor no númerico")