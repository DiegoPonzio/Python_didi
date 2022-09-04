from tkinter import END


class operaciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.i = 0

    def click(self, valor):
        self.i += 1
        self.ventana.entrada.insert(self.i, valor)

    def borrarC(self):
        self.ventana.entrada.delete(0,END)
        self.i = 0


    def borrar(self):
        self.i -= 1
        self.ventana.entrada.delete(self.i,END)


    def operacion(self):
        resultado = self.ventana.entrada.get()
        if self.i != 0:
            try:
                res = str(eval(resultado))
                self.ventana.entrada.delete(0, END)
                self.ventana.entrada.insert(0, res)
                self.i = len(res)
            except:
                res = "Error"
                self.ventana.entrada.delete(0,END)
                self.ventana.entrada.insert(0,res)
        else:
            pass
