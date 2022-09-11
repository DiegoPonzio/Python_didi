class Operaciones2:
    def __int__(self):
        self.contp = 0
        self.contc = 0
        self.cont = 0

    def prueba(self, tarjc, nump, numc, contp, contc):
        print("numero tarjeta player " + str(nump))
        print("nuemro tarjeta CPU " + str(numc))
        print("contadores p " + str(contp))
        print("contadores c " + str(contc))
        self.contp = contp
        self.contc = contc


    def Partida(self,marcp, marcc, tarjp, tarjc, cartap, cartac, contp, contc):
        self.contp = contp
        self.contc = contc

        if cartap == cartac:
            contc += 0
            contp += 0

            marcc.config(text="Contador CPU: " + str(contc))
            marcp.config(text="Contador Player: " + str(contp))

            tarjc.destroy()
            tarjp.destroy()

        elif cartap == 3 and cartac == 2:
            contp += 1
            marcp.config(text="Contador Player: " + str(contp))
            tarjc.destroy()
            tarjp.destroy()
        elif cartac == 3 and cartap == 2:
            contc += 1
            marcc.config(text="Contador CPU: " + str(contc))
            tarjc.destroy()
            tarjp.destroy()
        elif cartap == 2 and cartac == 1:
            contp += 1
            marcp.config(text="Contador Player: " + str(contp))
            tarjc.destroy()
            tarjp.destroy()
        elif cartac == 2 and cartap == 1:
            contc += 1
            marcc.config(text="Contador CPU: " + str(contc))
            tarjc.destroy()
            tarjp.destroy()
        elif cartap == 1 and cartap == 3:
            contp += 1
            marcp.config(text="Contador Player: " + str(contp))
            tarjc.destroy()
            tarjp.destroy()
        elif cartac == 1 and cartap == 3:
            contc += 1
            marcc.config(text="Contador CPU: " + str(contc))
            tarjc.destroy()
            tarjp.destroy()

        if contp == 3:
            print("ganador jugador")
            # regresarmos a la pagina principal
        elif contc == 3:
            print("ganadro cpu")
            # regresamos al estado anterior
        #elif cont == 5:
            #print("Empate")

