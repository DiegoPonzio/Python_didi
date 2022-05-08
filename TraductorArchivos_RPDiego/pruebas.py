import re

#prubas de la construccion del programa
#with open("dicc.txt", "r", encoding="utf8") as archivolec:

    #lineas =archivolec.readlines()
    #print(lineas)
    #archivolec.close()
#texto = ""
#pale = []
#dicc = {}

#for k in lineas:
    #corte = k.split("::")
    #pale.append(corte)
    #print(corte)
    #print(i)
    #for o in corte:
        #seg = o.split("\n")
        #pale.append(seg)
        #print(seg)

#for j in pale:
     #x = j
     #y = x[0]
     #z = x[1]
     #dicc[y] = z

#print(x)
#for o in dicc:
    #print( o + " : " + dicc[o].replace("\n", ""))

#for i in dicc:
    #texto += i + " : " + dicc[i].replace("\n", "") + "\n"

#frase = "rojo"
#text = "rojo : red\nrosa : pink\n"
#letra = "r"
#patron = re.compile(letra + "\w+ : +\w+\\n")
#patron2 = re.compile(frase + " : +\w+\\n")
#resultado = re.findall(patron2, text)
#resultados = re.findall(patron, text)
#resultados = re.fullmatch(patron,texto)

#print(len(frase))
#print(resultados)
#print(*resultado)
#print(texto)
#print(*dicc)
#print(pale)
dicc = {"azul": "blue", "mar": "sea"}

frase = "azul mar"
fraset = frase
patron = r"\W+"
part = re.split(patron, frase)

for j in part:
    for i in dicc:
        if j == i:
            fraset = fraset.replace(j,dicc[i])

print(fraset)
texto = ""
paln = "azul"
ingn = "ocean"
error = 0

for k in dicc:
    if k == paln:
        dicc[k] = ingn
        error == 0
        break
    else:
        error = 1

if error == 1:
    print("La palabra que desea modificar no se encuantra")
for i in dicc:
    texto += i + "::" + dicc[i].replace("\n", "") + "\n"

print(texto)

#with open ("dicc.txt", "w", encoding="utf8") as update:
    #update.write(texto)
    #update.close()
