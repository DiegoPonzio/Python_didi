from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Button
from tkinter import ttk
from operaciones import *
from PIL import Image
from PIL import ImageTk


class Interfaz:
    def __init__(self, ventana):
        def Partida(self,cartap, cartac):
            # piedra = 1
            # papel = 2
            # tijera = 3
            cont = 0
            contp = 0
            contc = 0

            if cartap == cartac:
                contc += 0
                contp += 0
                self.contadorc.config(text="Contador CPU: " + str(contc))
                self.contadorp.config(text="Contador CPU: " + str(contp))

            elif cartap == 3 and cartac == 2:
                contp += 1
                self.contadorp.config(text="Contador CPU: " + str(contp))
            elif cartac == 3 and cartap == 2:
                contc += 1
                self.contadorc.config(text="Contador CPU: " + str(contc))
            elif cartap == 2 and cartac == 1:
                contp += 1
                self.contadorp.config(text="Contador CPU: " + str(contp))
            elif cartac == 2 and cartap == 1:
                contc += 1
                self.contadorc.config(text="Contador CPU: " + str(contc))
            elif cartap == 1 and cartap == 3:
                contp += 1
                self.contadorp.config(text="Contador CPU: " + str(contp))
            elif cartac == 1 and cartap == 3:
                contc += 1
                self.contadorc.config(text="Contador CPU: " + str(contc))

            if contp == 3:
                print("ganador jugador")
                # regresarmos a la pagina principal
            elif contc  == 3:
                print("ganadro cpu")
                # regresamos al estado anterior
            elif cont == 5:
                print("Empate")

            self.cont += 1

        self.ventana = ventana
        operaciones = Operaciones(self)
        self.cont = 0
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
        self.img = Image.open("media/baraja.png").resize((186,260), Image.ANTIALIAS)
        self.imgPI = ImageTk.PhotoImage(self.img)
        self.imgp = Image.open("media/papel.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIp = ImageTk.PhotoImage(self.imgp)
        self.imgpd = Image.open("media/piedra.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIpd = ImageTk.PhotoImage(self.imgpd)
        self.imgt = Image.open("media/tijera.png").resize((186, 260), Image.ANTIALIAS)
        self.imgPIt = ImageTk.PhotoImage(self.imgt)
        self.txtp = Label(ventana, text="Piedra Papel o Tijera")
        self.txtp.grid(row=0, column=0)
        self.baraja = Button(ventana, image=self.imgPI, command=operaciones.Juego)
        self.baraja.grid(row=2,column=1)
        self.txt = Label(ventana, text="descripcion del juego")
        self.txt.grid(row=2, column=2)
        self.contadorp = Label(ventana)
        self.contadorc = Label(ventana)
        self.carta1c = Label(ventana, image= self.imgPI)
        self.carta2c = Label(ventana, image= self.imgPI)
        self.carta3c = Label(ventana, image= self.imgPI)
        self.carta4c = Label(ventana, image= self.imgPI)
        self.carta5c = Label(ventana, image= self.imgPI)
        self.vs = Label(text="vs")
        self.carta1p = Button(ventana)
        if self.carta1pa == 1:
            self.carta1p.config(image=self.imgPIpd, command= lambda : Partida(self, self.carta1pa,self.carta1ca))
        elif self.carta1pa == 2:
            self.carta1p.config(image=self.imgPIp, command= lambda : Partida(self, self.carta1pa,self.carta1ca))
        elif self.carta1pa == 3:
            self.carta1p.config(image=self.imgPIt, command= lambda : Partida(self,self.carta1pa,self.carta1ca))
        self.carta2p = Button(ventana)
        if self.carta2pa == 1:
            self.carta2p.config(image=self.imgPIpd, command= lambda : Partida(self,self.carta2pa,self.carta2ca))
        elif self.carta2pa == 2:
            self.carta2p.config(image=self.imgPIp, command= lambda : Partida(self,self.carta2pa,self.carta2ca))
        elif self.carta2pa == 3:
            self.carta2p.config(image=self.imgPIt, command= lambda : Partida(self,self.carta2pa,self.carta2ca))
        self.carta3p = Button(ventana)
        if self.carta3pa == 1:
            self.carta3p.config(image=self.imgPIpd, command= lambda : Partida(self,self.carta3pa,self.carta3ca))
        elif self.carta3pa == 2:
            self.carta3p.config(image=self.imgPIp, command= lambda : Partida(self,self.carta3pa,self.carta3ca))
        elif self.carta3pa == 3:
            self.carta3p.config(image=self.imgPIt, command= lambda : Partida(self,self.cartapa,self.carta2ca))
        self.carta4p = Button(ventana)
        if self.carta4pa == 1:
            self.carta4p.config(image=self.imgPIpd, command= lambda : Partida(self,self.carta4pa,self.carta4ca))
        elif self.carta4pa == 2:
            self.carta4p.config(image=self.imgPIp, command= lambda : Partida(self,self.carta4pa,self.carta4ca))
        elif self.carta4pa == 3:
            self.carta4p.config(image=self.imgPIt, command= lambda : Partida(self,self.carta4pa,self.carta4ca))
        self.carta5p = Button(ventana)
        if self.carta5pa == 1:
            self.carta5p.config(image=self.imgPIpd,command= lambda : Partida(self,self.carta5pa,self.carta5ca))
        elif self.carta5pa == 2:
            self.carta5p.config(image=self.imgPIp, command= lambda : Partida(self,self.carta5pa,self.carta5ca))
        elif self.carta5pa == 3:
            self.carta5p.config(image=self.imgPIt,command= lambda : Partida(self,self.carta5pa,self.carta5ca))



def main():
    from tkinter import Tk
    ventana = Tk()
    ventana.geometry('950x600')
    ventana.title("Piedra Papel o Tijera !!")
    ventana.resizable(0,0)
    app = Interfaz(ventana)
    ventana.mainloop()


if __name__ == '__main__':
    main()



#    def marcp(self):
        #contp = self.contp
        #return contp

    #def marcc(self):
        #contc = self.contc
        #3return contc

    #def mar(self):
        #marc = self.cont
        #return marc#