from tkinter import Frame,Label
import random
from PIL import Image
from PIL import ImageTk

class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.contadorc = 0
        self.contadorp = 0
        #self.imgp = Image.open("./media/papel.png").resize((186, 260))
        #self.imgPIp = ImageTk.PhotoImage(self.imgp)

    def Juego(self):
        self.ventana.txt.destroy()
        self.ventana.baraja.destroy()
        self.ventana.txtp.destroy()
        self.ventana.contadorp.grid(row=0, column=2)
        self.ventana.contadorc.grid(row=0, column=4)
        self.ventana.carta1c.grid(row = 1, column=1)
        self.ventana.carta2c.grid(row=1, column=2)
        self.ventana.carta3c.grid(row=1, column=3)
        self.ventana.carta4c.grid(row=1, column=4)
        self.ventana.carta5c.grid(row=1, column=5)
        self.ventana.vs.grid(row=2,column=3)
        self.ventana.carta1p.grid(row=3, column=1)
        self.ventana.carta2p.grid(row=3, column=2)
        self.ventana.carta3p.grid(row=3, column=3)
        self.ventana.carta4p.grid(row=3, column=4)
        self.ventana.carta5p.grid(row=3, column=5)


    def caso1(self):
        print("piedra")

    def caso2(self):
        print("papel")

    def caso3(self):
        print("tijera")