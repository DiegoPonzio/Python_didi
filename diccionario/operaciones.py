import re

class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.texto = "Palabra : Traduccion \n"
        self.dicc = {}
        listap = ""
        intr = 0
        with open("dicc.txt", "r", encoding="utf8") as archivolec:
            lineas = archivolec.readlines()
            #print(lineas)
            archivolec.close()

        pale = []
        for k in lineas:
            corte = k.split("::")
            pale.append(corte)

        for j in pale:
            x = j
            y = x[0]
            z = x[1]
            a = x[2]
            b = x[3]
            #z = ""
            self.dicc[y] = [z,a,b]
        for i in self.dicc:
            for k in self.dicc[i]:
                self.texto += i + " : " + k  + " " + "\n"

    def verDicc(self):
        self.ventana.resultado.configure(text=self.texto)

    def busqueda(self):
        result = ""
        pal = self.ventana.buscador.get()
        if pal == "":
            self.ventana.resultado.configure(text="No se ha escrito nada")
            self.ventana.buscador.focus()
        else:
            if len(pal) == 1:
                patron = re.compile("[\\n,\s\\n,\s\\n\s,\\n\s]" + pal + "\w+ : +\w+\\n")
                res = re.findall(patron, self.texto)
                if len(res) != 0:
                    for yu in res:
                        result += yu
                    self.ventana.resultado.configure(text="Resultados: " + result.replace("\n\n","\n"))
                else:
                    self.ventana.resultado.configure(text="No hay coincidencias")
                print(res)
            else:
                patron = re.compile("[\\n,\\r\\n]" + pal + "[\w : , : , : ]+\w+\\n")
                res = re.findall(patron, self.texto)
                print(res)
                if len(res) != 0:
                    for you in res:
                        result += you
                    self.ventana.resultado.configure(text="Resultados:" + result.replace("\n\n","\n"))
                else:
                    self.ventana.resultado.configure(text="No hay coincidencias")

    def busquedaA(self):
        result = ""
        pal = self.ventana.buscador.get()
        if pal == "":
            self.ventana.resultado.configure(text="No se ha escrito nada")
            self.ventana.buscador.focus()
        else:
            if len(pal) == 1:
                patron = re.compile("[\\n,\s\\n,\s\\n\s,\\n\s]" + pal + "\w+ : +\w+")
                res = re.findall(patron, self.texto)
                if len(res) != 0:
                    for yu in res:
                        result += yu
                    self.ventana.resultado.configure(text="Resultados (ingles, frances, aleman): " + result.replace("\n\n","\n"))
                else:
                    self.ventana.resultado.configure(text="No hay coincidencias")
                print(self.texto)
            else:
                patron = re.compile("[\\n,\\r\\n]" + pal + "[\w : , : , : ]+\w+")
                res = re.findall(patron, self.texto)
                print(self.texto)
                if len(res) != 0:
                    for you in res:
                        result += you
                    self.ventana.resultado.configure(text="Resultados: (ingles, frances, aleman)" + result.replace("\n\n","\n"))
                else:
                    self.ventana.resultado.configure(text="No hay coincidencias")


    def trad(self):
        dicct = self.dicc
        frase = self.ventana.buscador.get()
        fraset = frase
        patron = r"\W+"
        part = re.split(patron, frase)
        for j in part:
            for i in dicct:
                if j == i:
                    fraset = fraset.replace(j, dicct[i])

        self.ventana.resultado.configure(text="La frase en español es: " + frase + "\nLa frase en ingles es: " + fraset.replace("\n",""))