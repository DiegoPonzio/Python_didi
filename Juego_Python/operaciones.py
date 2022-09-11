from tkinter import Label,Button
from PIL import Image,ImageTk
from operaciones2 import *
import random

class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.carta1pa = random.randint(1, 3)
        self.carta2pa = random.randint(1, 3)
        self.carta3pa = random.randint(1, 3)
        self.carta4pa = random.randint(1, 3)
        self.carta5pa = random.randint(1, 3)
        self.carta1ca = random.randint(1, 3)
        self.carta2ca = random.randint(1, 3)
        self.carta3ca = random.randint(1, 3)
        self.carta4ca = random.randint(1, 3)
        self.carta5ca = random.randint(1, 3)
        self.contp = 0
        self.contc = 0
        self.cont = 0


    def Juego(self, imgPI, imgPIpd, imgPIp, imgPIt):
        operaciones = Operaciones2()
        self.ventana.txt.destroy()
        self.ventana.baraja.destroy()
        self.ventana.txtp.destroy()

        self.contadorp = Label(self.ventana.pelea, text="Contador Player: 0")
        self.contadorc = Label(self.ventana.pelea, text="Contador CPU: 0")
        self.carta1c = Label(self.ventana.pelea, image=imgPI)
        self.carta2c = Label(self.ventana.pelea, image=imgPI)
        self.carta3c = Label(self.ventana.pelea, image=imgPI)
        self.carta4c = Label(self.ventana.pelea, image=imgPI)
        self.carta5c = Label(self.ventana.pelea, image=imgPI)

        self.vs = Label(self.ventana.pelea, text="vs", font=("Arial",72))

        self.contadorp.grid(row=0, column=2)
        self.contadorc.grid(row=0, column=4)
        self.carta1c.grid(row=1, column=1)
        self.carta2c.grid(row=1, column=2)
        self.carta3c.grid(row=1, column=3)
        self.carta4c.grid(row=1, column=4)
        self.carta5c.grid(row=1, column=5)
        self.vs.grid(row=2, column=3)

        self.carta1p = Button(self.ventana.pelea)
        self.carta2p = Button(self.ventana.pelea)
        self.carta3p = Button(self.ventana.pelea)
        self.carta4p = Button(self.ventana.pelea)
        self.carta5p = Button(self.ventana.pelea)

        if self.carta1pa == 1:
            self.carta1p.config(image=imgPIpd, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta1p, self.carta1c, self.carta1pa, self.carta1ca, self.contp, self.contc))
            #self.contp = operaciones.marcp()
            #self.contc = operaciones.marcc()
        elif self.carta1pa == 2:
            self.carta1p.config(image=imgPIp, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta1p,self.carta1c, self.carta1pa, self.carta1ca, self.contp, self.contc))
            #self.contp = operaciones.marcp()
            #self.contc = operaciones.marcc()
        elif self.carta1pa == 3:
            self.carta1p.config(image=imgPIt, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta1p,self.carta1c, self.carta1pa, self.carta1ca, self.contp, self.contc))
            #self.contp = operaciones.marcp()
            #self.contc = operaciones.marcc()

        if self.carta2pa == 1:
            self.carta2p.config(image=imgPIpd, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta2p,self.carta2c, self.carta2pa, self.carta2ca, self.contp, self.contc))
        elif self.carta2pa == 2:
            self.carta2p.config(image=imgPIp, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta2p,self.carta2c, self.carta2pa, self.carta2ca, self.contp, self.contc))
        elif self.carta2pa == 3:
            self.carta2p.config(image=imgPIt, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta2p,self.carta2c, self.carta2pa, self.carta2ca, self.contp, self.contc))

        if self.carta3pa == 1:
            self.carta3p.config(image=imgPIpd, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta3p,self.carta3c, self.carta3pa, self.carta3ca, self.contp, self.contc))
        elif self.carta3pa == 2:
            self.carta3p.config(image=imgPIp, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta3p,self.carta3c, self.carta3pa, self.carta3ca, self.contp, self.contc))
        elif self.carta3pa == 3:
            self.carta3p.config(image=imgPIt, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta3p,self.carta3c, self.carta3pa, self.carta3ca, self.contp, self.contc))

        if self.carta4pa == 1:
            self.carta4p.config(image=imgPIpd, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta4p,self.carta4c, self.carta4pa, self.carta4ca, self.contp, self.contc))
        elif self.carta4pa == 2:
            self.carta4p.config(image=imgPIp, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta4p,self.carta4c, self.carta4pa, self.carta4ca, self.contp, self.contc))
        elif self.carta4pa == 3:
            self.carta4p.config(image=imgPIt, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta4p,self.carta4c, self.carta4pa, self.carta4ca, self.contp, self.contc))

        if self.carta5pa == 1:
            self.carta5p.config(image=imgPIpd, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta5p,self.carta5c, self.carta5pa, self.carta5ca, self.contp, self.contc))
        elif self.carta5pa == 2:
            self.carta5p.config(image=imgPIp, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta5p,self.carta5c, self.carta5pa, self.carta5ca, self.contp, self.contc))
        elif self.carta5pa == 3:
            self.carta5p.config(image=imgPIt, command=lambda: operaciones.Partida(self.contadorp, self.contadorc,self.carta5p,self.carta5c, self.carta5pa, self.carta5ca, self.contp, self.contc))

        self.carta1p.grid(row=3, column=1)
        self.carta2p.grid(row=3, column=2)
        self.carta3p.grid(row=3, column=3)
        self.carta4p.grid(row=3, column=4)
        self.carta5p.grid(row=3, column=5)



    def suma(self):
        a = 186
        b = 24
        c =  a+b
        self.ventana.resultado.configure(text=c)
        self.txt = Label(self.ventana.inferior, text="prueba")
        self.txt.grid(column=3, row=1)

    def resta(self):
        a = 186
        b = 24
        c =  a-b
        self.ventana.resultado.configure(text=c)

    def multiplicacion(self):
        a = 186
        b = 24
        c = a*b
        self.ventana.resultado.configure(text=c)

    def division(self):
        a = 186
        b = 24
        c = a/b
        self.ventana.resultado.configure(text=c)

    def divisionParteEntera(self):
        a = 186
        b = 24
        c =  a%b
        self.ventana.resultado.configure(text=c)

    def divisionResto(self):
        a = 186
        b = 24
        c = a%b
        self.ventana.resultado.configure(text=c)