from tkinter import *
from tkinter import ttk
from operaciones2 import *

class Interfaz2:
    def __init__(self, ventana2):
        self.ventana2 = ventana2
        operaciones2 = Operaciones2(self)
        self.texto1 = Label(ventana2, text="Agergar palabras español - ingles")
        self.texto1.pack()
        self.texto2 = Label(ventana2, text="Ingrese la palabra en español")
        self.texto2.pack()
        self.pales = ttk.Entry(ventana2)
        self.pales.pack()
        self.texto3 = Label(ventana2, text="Ingrese la palabra en ingles")
        self.texto3.pack()
        self.palin = ttk.Entry(ventana2)
        self.palin.pack()
        self.boton1 = Button(ventana2, text="Agregar", bg="blue", command=operaciones2.agregarp)
        self.boton1.pack()
        self.boton3 = Button(ventana2, text="Modificar", bg="blue", command=operaciones2.modificar)
        self.boton3.pack()
        self.boton2 = Button(ventana2, text="Salir", bg="blue", command=ventana2.destroy)
        self.boton2.pack()
        self.resultado = Label(ventana2, text="", bg="orange", font=("Arial", 12))
        self.resultado.pack()

def add():
    from tkinter import Tk
    ventana2 = Tk()
    ventana2.geometry('500x300')
    ventana2.title("Agregar al diccionario Ingles - Español")
    app = Interfaz2(ventana2)
    ventana2.mainloop()
