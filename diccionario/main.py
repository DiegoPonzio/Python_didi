from tkinter import *
from tkinter import ttk

#import operaciones2
from operaciones import *
#from operaciones2 import *
#import gui3





class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        operaciones = Operaciones(self)
        self.texto1 = Label(ventana, text="Bienvenido al diccionario", font=("Arial Bold", 20))
        self.texto1.pack()
        self.buscador = ttk.Entry()
        self.buscador.pack()
        self.boton6 = Button(ventana, text="Buscar", bg="blue", command=operaciones.busquedaA)
        self.boton6.pack()
        self.boton2 = Button(ventana, text="Ver Diccionario", bg="blue", command=operaciones.verDicc)
        self.boton2.pack()
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


