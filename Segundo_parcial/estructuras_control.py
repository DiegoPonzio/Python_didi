#Diccionario de sinonimos

dicc={"previo":["anterior","antes de"]}
bandera = 1
#bandera2 = 1
#trad = []

#print(dicc)

nuevo = ["monitvo","sircunstancia"]

dicc.setdefault("razón",nuevo)

#print(dicc)

while bandera == 1:
    sinonimo = []
    bandera2 = 1
    print("----------------------------------")
    print("Diccionario de sinonimos")
    print(" 1.Agregar palabra y sus sinonimos")
    print(" 2.Agregar sinonimos")
    print(" 3.Imprimir diccionario")
    print(" 4.Salir")
    print("-----------------------------------")
    select = int(input("Seleccione un numero: "))

    if select == 1:
        pal = 0
        while bandera2 == 1:
            x = input("Ingrese la palabra que desea agregar: ")
            y = input("Ingrese el sinonimo de la palabra: ")
            for i in dicc:
                if i == x:
                    pal = 0
                else:
                    pal = 2

            if pal == 2:
                bandera3 = 1
                sinonimo.append(y)
                while bandera3 == 1:
                    print("----------------------------------")
                    print("Diccionario de sinonimos")
                    print(" 1.Agregar nuevo sinonimo")
                    print(" 2.Salir")
                    print("-----------------------------------")
                    select2 = int(input("Seleccione un numero: "))
                    if select2 == 1:
                        z = input("Ingrese un nuevo sinonimo de la palabra: ")
                        sinonimo.append(z)
                        select2 = 0
                        break
                    elif select2 == 2:
                        bandera3 = 2
                        break
                    else:
                        print("El valor que eligio no existe vuelva a intentar")
                        select2 = 0
                        break
                dicc.setdefault(x, sinonimo)
                print(dicc)
                bandera2 = 2
                break
            else:
                print("La palabra que deseas agregar ya existe en el diccionario")
        select = 0
    elif select == 2:
        pal = 0
        select2 = 0
        bandera2 = 1
        while bandera2 == 1:
            x = input("Ingrese la palabra a la cual le agregara sinonimos: ")
            y = input("Ingrese el nuevo sinonimo de la palabra: ")
            for word in dicc:
                if word == x:
                   pal = 0
                else:
                    pal = 2

            if pal == 0:
                bandera3 = 1
                for sim in dicc[x]:
                    sinonimo.append(sim)
                sinonimo.append(y)
                while bandera3 == 1:
                    print("----------------------------------")
                    print("Diccionario de sinonimos")
                    print(" 1.Agregar nuevo sinonimo")
                    print(" 2.Salir")
                    print("-----------------------------------")
                    select2 = int(input("Seleccione un numero: "))
                    if select2 == 1:
                        z = input("Ingrese un nuevo sinonimo de la palabra: ")
                        sinonimo.append(z)
                        select2 = 0
                        break
                    elif select2 == 2:
                        bandera3 = 2
                        break
                    else:
                        print("El valor que eligio no existe vuelva a intentar")
                        select2 = 0

                dicc[x] = sinonimo
                print(dicc)
                bandera2 = 2
                break
            else:
                print("La palabra no existe en el diccionario")
                break

        select = 0
    elif select == 3:
        for q in dicc:
            for t in dicc[q]:
                print(q, ": ", t)
        select = 0
    elif select == 4:
        print("-------------")
        print("vuelva pronto")
        print("-------------")
        bandera = 2

    else:
        print("El valor que eligio no existe vuelva a intentar")