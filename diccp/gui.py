from tkinter import *
from operaciones import *

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        operaciones=Operaciones(self)
        self.superior=Frame(self.ventana)
        self.superior.pack(side=TOP)
        self.valores = Label(self.superior, text=" a=186\nb=24", font=("Arial Bold", 20))
        self.valores.pack(padx=15, pady=15, side=LEFT)
        self.resultado = Label(self.superior, text="resultado: ", width=25, height=2, bg="white", font=("Arial", 12))
        self.resultado.pack(padx=15, pady=15, side=RIGHT)
        self.inferior=Frame(self.ventana)
        self.inferior.pack(side=TOP)
        self.btn_suma = Button(self.inferior, text="+", bg="orange", height=2, width=5, command=operaciones.suma)
        self.btn_resta = Button(self.inferior, text="-", bg="orange", height=2, width=5, command=operaciones.resta)
        self.btn_multip = Button(self.inferior, text="*", bg="orange", height=2, width=5, command=operaciones.multiplicacion)
        self.btn_divis = Button(self.inferior, text="/", bg="orange", height=2, width=5, command=operaciones.division)
        self.btn_div_ent = Button(self.inferior, text="//", bg="orange", height=2, width=5, command=operaciones.divisionParteEntera)
        self.btn_div_resto = Button(self.inferior, text="%", bg="orange", height=2, width=5, command=operaciones.divisionResto)
        self.btn_suma.grid(column=0, row=1)
        self.btn_resta.grid(column=1, row=1)
        self.btn_multip.grid(column=2, row=1)
        self.btn_divis.grid(column=0, row=2)
        self.btn_div_ent.grid(column=1, row=2)
        self.btn_div_resto.grid(column=2, row=2)

def main():
    from tkinter import Tk
    ventana = Tk()
    ventana.geometry('500x300')
    ventana.title("Hagamos cuentas")
    app = Interfaz(ventana)
    ventana.mainloop()


if __name__ == '__main__':
    main()