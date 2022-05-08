class Operaciones2 :
    def __init__(self, ventana2):
        self.ventana2 = ventana2

        self.dicc = {}
        with open("dicc.txt", "r", encoding="utf8") as archivolec:
            lineas = archivolec.readlines()
            archivolec.close()

        pale = []
        for k in lineas:
            corte = k.split("::")
            pale.append(corte)

        for j in pale:
            x = j
            y = x[0]
            z = x[1]
            # z = ""
            self.dicc[y] = z


    def agregarp(self):
        espa = self.ventana2.pales.get()
        ing = self.ventana2.palin.get()
        if espa != "" and ing != "":
            with open("dicc.txt", "a", encoding="utf8") as addp:
                addp.write(espa + "::" + ing + "\n")
                addp.close()

            self.ventana2.resultado.configure(text="Se guardo la palabra: " + espa + " con su respectiva en ingles: " + ing + "\nCierre el programa y vuelva a iniciar para ver las actualizaciones")
        else:
            self.ventana2.resultado.configure(text="No se ha ingreado ningun valor")
            self.ventana2.pales.focus()
            self.ventana2.palin.focus()

    def modificar(self):
        espan = self.ventana2.pales.get()
        ingn = self.ventana2.palin.get()
        error = 0
        texto = ""
        if espan != "" and ingn != "":
            for k in self.dicc:
                if k == espan:
                    self.dicc[k] = ingn
                    error = 0
                    break
                else:
                    error = 1
            if error == 1:
                self.ventana2.resultado.configure(text="La palabra que desea modificar no existe")
                self.ventana2.pales.focus()
            else:
                self.ventana2.resultado.configure(text="Se ha modificado la palabra correctamente\nCierre el programa para ver las actualizaciones")

            for i in self.dicc:
                texto += i + "::" + self.dicc[i].replace("\n", "") + "\n"

            with open("dicc.txt", "w", encoding="utf8") as update:
                update.write(texto)
                update.close()
        else:
            self.ventana2.resultado.configure(text="No se ha ingreado ningun valor")
            self.ventana2.pales.focus()
            self.ventana2.palin.focus()
