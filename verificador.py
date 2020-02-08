"""
Created on Wed Feb  5 08:29:58 2020

@author: Rudik Roberto Rompich
@class: Herramientas Tecnologicas
"""

lol = int(input("\n|BIENVENIDO AL VERFICADOR DE CODIGOS: | \n" +

            "SELECCIONE UNA OPCION: \n\n" +
            "1. VERIFICAR \n" +
            "2. DIGITO DE CONTROL\n" +
            "3. SALIR \n\n" +
            "OPCION:"))

while lol !=3:

 try:

    if lol ==1:

        x = int(input("¿Qué código quiere combrobar?: \n" +
                          "1. UPC \n" +
                          "2. ISBN - 10 \n" +
                          "3. ISBN - 13 \n" +
                          "4. NIT \n" +
                          "5. Salir\n" +
                          " Opción:"))
        while x != 5:

             if x ==1:
                 print("1")
             elif x ==2:
                 print("2")
             elif x ==3:
                 print("3")
             elif x ==4:
                 print("4")
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