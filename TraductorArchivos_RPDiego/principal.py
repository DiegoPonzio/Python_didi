from tkinter import *
from tkinter import ttk

import operaciones2
from operaciones import *
from operaciones2 import *
import ventana2





class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        operaciones = Operaciones(self)
        self.texto1 = Label(ventana, text="Bienvenido al diccionario", font=("Arial Bold", 20))
        self.texto1.pack()
        self.buscador = ttk.Entry()
        self.buscador.pack()
        self.boton5 = Button(ventana, text="Buscar", bg="blue", command=operaciones.busqueda)
        self.boton5.pack()
        self.boton1 = Button(ventana, text="Agregar/Modificar Palabras", bg="blue", command=ventana2.add)
        self.boton1.pack()
        self.boton2 = Button(ventana, text="Ver Diccionario", bg="blue", command=operaciones.verDicc)
        self.boton2.pack()
        self.boton3 = Button(ventana, text="Traducir Frase", bg="blue", command=operaciones.trad)
        self.boton3.pack()
        self.boton4 = Button(ventana, text="Salir", bg="blue", command=ventana.destroy)
        self.boton4.pack()
        self.resultado = Label(ventana, text="resultado: ", bg="orange", font=("Arial", 12))
        self.resultado.pack()

def main():
    from tkinter import Tk
    ventana = Tk()
    ventana.geometry('500x300')
    ventana.title("Diccionario Ingles - Español")
    app = Interfaz(ventana)
    ventana.mainloop()

if __name__ == '__main__':
    main()
