class Operaciones2 :
    def __init__(self, ventana2):
        self.ventana2 = ventana2

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