import pandas as pd

titanicv = pd.read_csv("titanic.csv.csv")

#print(titanicv.describe())

bandera = 0

while bandera == 0:
    print("-----------------------------------------------------------------------------------------")
    print("Bienvenido a pandas:")
    print("    1. Mostrar dimensiones del DataFrame,\n"
        "       el número de datos que contiene,\n"
        "       los nombres de sus columnas y filas,\n"
        "       los tipos de datos de las columnas,\n"
        "       las 10 primeras filas y las 10 últimas filas.")
    print("    2. Mostrar por pantalla los datos del pasajero con identificador 148.")
    print("    3. Mostrar por pantalla las filas pares del DataFrame.")
    print("    4. Mostrar por pantalla los nombres de las personas que iban en primera clase\n"
          "       ordenadas alfabéticamente.")
    print("    5. Mostrar los nombres de los pasajeros que el costo de su pasaje\n"
          "       osciló entre 70 a 170 dolares.")
    print("    6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.")
    print("    7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.")
    print("    8. Eliminar del DataFrame los pasajeros con edad desconocida.")
    print("    9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.")
    print("    10. Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.")
    print("    11. Mostrar por pantalla el porcentaje de menores y mayores de edad\n"
          "        que sobrevivieron en cada clase.")
    print("    12. Salir")
    print("-----------------------------------------------------------------------------------------")
    selct = int(input("Elige un número: "))

    if selct == 1:
        print("Las dimenciones del DataFrame son: ", titanicv.shape,
              "\n", titanicv.describe())
        print("Su tipo de datos son: ", type(titanicv))
        print("Sus columnas son: ", *list(titanicv.columns))
        print("Sus 10  primeros valores son:")
        print(titanicv.head(10))
        print("Sus ultimos 10 vaores son:")
        print(titanicv.tail(10))

    elif selct == 2:
        print("Los datos del pasajero 148 son:")
        print(titanicv.loc[147])

    elif selct == 3:
        print("Las filas pares son: ")
        par = titanicv.loc[:, 'PassengerId'] % 2 == 0
        ispar = titanicv.loc[par]
        print(ispar)

    elif selct == 4:
        print("Personas en primera clasde:")
        pc = titanicv.loc[:, "Pclass"] == 1
        alfa = titanicv.loc[pc]
        isalfa = alfa.sort_values("Name")
        print(isalfa)

    elif selct == 5:
        print("Pasajeros con costo de pasaje entre 70 a 170 dolares:")
        var = titanicv.loc[:, "Fare"] > 70
        var2 = var < 170
        isvar = titanicv.loc[var2]
        print(isvar)

    elif selct == 6:
        suv = titanicv.loc[:, "Survived"] == 1
        dead = titanicv.loc[:, "Survived"] == 0
        issuv = titanicv.loc[suv]
        isdead = titanicv.loc[dead]

        porsuv = (len(issuv) * 100) / 891
        pordead = (len(isdead) * 100) / 891

        print("Porcentaje de sobrevivientes: ", porsuv,"%")
        print("Porcentaje de bajas: ", pordead,"%")

    elif selct == 7:
        suv = titanicv.loc[:, "Survived"] == 1
        issuv = titanicv.loc[suv]

        p1 = titanicv.loc[:, "Pclass"] == 1
        p2 = titanicv.loc[:, "Pclass"] == 2
        p3 = titanicv.loc[:, "Pclass"] == 3
        isp1 = titanicv.loc[p1]
        isp2 = titanicv.loc[p2]
        isp3 = titanicv.loc[p3]

        suv1 = titanicv.loc[:, "Pclass"] == 1
        suv2 = titanicv.loc[:, "Pclass"] == 2
        suv3 = titanicv.loc[:, "Pclass"] == 3
        issuv1 = issuv.loc[suv1]
        issuv2 = issuv.loc[suv2]
        issuv3 = issuv.loc[suv3]

        porsuv1 = (len(issuv1) * 100) / len(isp1)
        porsuv2 = (len(issuv2) * 100) / len(isp2)
        porsuv3 = (len(issuv3) * 100) / len(isp3)

        print("Porcentaje de sobrevivientes 1° clase: ", porsuv1,"%")
        print("Porcentaje de sobrevivientes 2° clase: ", porsuv2,"%")
        print("Porcentaje de sobrevivientes 3° clase: ", porsuv3,"%")

    elif selct == 8:
        Age = list(titanicv["Age"])
        PassengerId = list(titanicv["PassengerId"])
        NAge = []
        i = 0
        while i < int(len(titanicv.index)):
            if Age[i] >= 18:
                pass
            elif 0 < Age[i] < 18:
                pass
            else:
                NAge.append(PassengerId[i] - 1)
            i += 1
        i = 0
        print(NAge)
        Actualizado = titanicv.drop(NAge)
        print("La tabla con los datos borrados es: ")
        print(Actualizado)
        print("El archivo fue guardado en un nuevo csv llamado Sin_Edad")
        Actualizado.to_csv('Sin_Edad.csv')

    elif selct == 9:
        p1 = titanicv.loc[:, "Pclass"] == 1
        p2 = titanicv.loc[:, "Pclass"] == 2
        p3 = titanicv.loc[:, "Pclass"] == 3
        isp1 = titanicv.loc[p1]
        isp2 = titanicv.loc[p2]
        isp3 = titanicv.loc[p3]

        print("Promedio de edad 1° clase:\n", isp1.Age.describe())
        print("Promedio de edad 2° clase:\n", isp2.Age.describe())
        print("Promedio de edad 3° clase:\n", isp3.Age.describe())

    elif selct == 10:
        Age = list(titanicv["Age"])
        PassengerId = list(titanicv["PassengerId"])
        NAge = []
        i = 0
        while i < int(len(titanicv.index)):
            if Age[i] >= 18:
                pass
            elif 0 < Age[i] < 18:
                pass
            else:
                NAge.append(PassengerId[i] - 1)
            i += 1
        i = 0
        print(NAge)
        Actualizado = titanicv.drop(NAge)
        i = 0
        edadB = []
        while i < len(Actualizado.index):
            if AAge[i] >= 18:
                edadB.append(1)
            else:
                edadB.append(0)
            i += 1
        MayoresMenores = Actualizado.assign(MayordeEdad=edadB)
        print("La tabla con la nueva collumna")
        print(MayoresMenores)
        print("El archivo fue guardado en un nuevo csv llamado MayoresMenores")
        MayoresMenores.to_csv('MayoresMenores.csv')

    elif selct == 11:
        p1 = titanicv.loc[:, "Pclass"] == 1
        p2 = titanicv.loc[:, "Pclass"] == 2
        p3 = titanicv.loc[:, "Pclass"] == 3
        suv = titanicv.loc[:, "Survived"] == 1


    elif selct == 12:
        print("-----------------------------------------------------------------------------------------")
        print("Vuelva Pronto")
        print("-----------------------------------------------------------------------------------------")
        bandera = 1

    else:
        print("El valor seleccionado no exite intente de nuevo")





