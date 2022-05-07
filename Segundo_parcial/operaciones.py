class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana

    def suma(self):
        a = 186
        b = 24
        c =  a+b
        self.ventana.resultado.configure(text=c)

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