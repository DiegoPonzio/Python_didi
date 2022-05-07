varfn = []
invetida = []
frase =input("Introduce una frase: ")

palabras = frase.split(" ")

print(palabras)

for i in palabras:
    j = i[::-1]
    varfn += ["La palabra: ", i, " de foma inversa es: ", j, "\n"]

print(*varfn)
palabra = input("ponga una palabra")
inv=[]
k = 0
for j in palabra:
    inv.append(j)
    k += 1
invt = ""
h = k-1;
print(inv)
bandera = 1

while bandera == 1:
    if h < 0:
        bandera = 2
    else:
        invt += inv[h]
        h-=1

print(invt)