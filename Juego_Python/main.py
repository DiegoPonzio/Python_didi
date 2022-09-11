from tkinter import *
from operaciones import *
from PIL import Image,ImageTk

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        operaciones=Operaciones(self)
        self.pelea = Frame(ventana)
        self.pelea.grid(column=1, row=1)
        self.img = Image.open("media/baraja.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPI = ImageTk.PhotoImage(self.img)
        self.imgp = Image.open("media/papel.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIp = ImageTk.PhotoImage(self.imgp)
        self.imgpd = Image.open("media/piedra.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIpd = ImageTk.PhotoImage(self.imgpd)
        self.imgt = Image.open("media/tijera.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIt = ImageTk.PhotoImage(self.imgt)
        self.txtp = Label(ventana, text="Piedra Papel o Tijera")
        self.txtp.grid(row=0, column=0)
        self.baraja = Button(ventana, image=self.imgPI, command=lambda: operaciones.Juego(self.imgPI,self.imgPIpd,self.imgPIp, self.imgPIt))
        self.baraja.grid(row=2, column=1)
        self.txt = Label(ventana, text="descripcion del juego")


def main():
    from tkinter import Tk
    ventana = Tk()
    ventana.geometry('960x670')
    ventana.title("Piedra Papel o Tijera !!")
    app = Interfaz(ventana)
    ventana.mainloop()


if __name__ == '__main__':
    main()
