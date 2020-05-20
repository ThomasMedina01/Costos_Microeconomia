import sys
def pedirNumeroEntero():
 
    correcto=False
    num=0
    intento = 1
    while(not correcto):
        try:
            num = int(input("Comenzando desde 0, ¿Cuantos niveles de produccion desea registrar? "))
            correcto=True
        except ValueError:
            print('Error, Solo se aceptan numeros enteros, intentalo nuevamente')
            print("♣-♦-" * 33)
            intento = intento + 1
            if intento > 5:
                print("Sobrepasaste el limite de intentos permitidos (5), ejecuta el programa nuevamente.")
                print("♣-♦-" * 33)
                sys.exit()
     
    return num

def pedircosto():
 
    correcto=False
    num=0
    intento = 1
    while(not correcto):
        try:
            num = float(input("Escribe el costo total: "))
            correcto=True
        except ValueError:
            print('Error, Solo se aceptan valores numericos, intentalo nuevamente')
            print("♣-♦-" * 33)
            intento = intento + 1
            if intento > 5:
                print("Sobrepasaste el limite de intentos permitidos (5), ejecuta el programa nuevamente.")
                print("♣-♦-" * 33)
                sys.exit()
     
    return num

def pedirprecio():
 
    correcto=False
    num=0
    intento = 1
    while(not correcto):
        try:
            num = float(input("Ingresa el precio de venta: "))
            correcto=True
        except ValueError:
            print('Error, Solo se aceptan valores numericos, intentalo nuevamente')
            print("♣-♦-" * 33)
            intento = intento + 1
            if intento > 5:
                print("Sobrepasaste el limite de intentos permitidos (5), ejecuta el programa nuevamente.")
                print("♣-♦-" * 33)
                sys.exit()
     
    return num

def pedirOpcion():
 
    correcto=False
    num=0
    intento = 1
    while(not correcto):
        try:
            num = int(input("Escribe cualquier numero para hacer otro calculo o presiona 0 para salir del sistema: "))
            correcto=True
        except ValueError:
            print('Error, Solo puedes ingresar numeros enteros')
            print("♣-♦-" * 33)
            intento = intento + 1
            if intento > 5:
                print("Sobrepasaste el limite de intentos permitidos (5), ejecuta el programa nuevamente.")
                print("♣-♦-" * 33)
                sys.exit()
     
    return num



class Tabla():
    def __init__(self, q, ct, pv, ctan, cft):
        self.q = q
        self.ct = ct
        self.pv = pv
        self.ctan = ctan
        self.cft = cft

    #poner los if para la segunda vuelta
    def vertablainicial(self):
        self.cft = self.ct #solo funciona para la primer columna
        self.cvt = self.ct - self.cft
        self.cmt = 0
        self.cmv = 0
        self.cmf = 0
        self.cm = 0
        self.it = 0
        self.im = self.pv
        self.bop = self.it - self.ct
        self.formato = f"{'Produccion':<10} {'Costo_ft':<10} {'Costo_vt':<10} {'costo_t':<10} {'Costo_mt':<10} {'Costo_mv':<10} {'Costo_mf':<10} {'Costo_mar':<10} {'Ingreso_t':<10} {'ingreso_m':<10} {'Beneficios o perdidas':<15} \n"
        self.formato += (f"{self.q: 5} {self.cft: 10} {self.cvt: 10} {self.ct: 10} {self.cmt: 10} {self.cmv: 10} {self.cmf: 10} {self.cm: 10} {self.it: 10} {self.im: 10} {self.bop: 10}\n")
        return self.formato

    def vertablafinal(self):
        self.cvt = self.ct - self.cft
        self.cm = (self.ct - self.ctan/1)
        self.ig = self.q * self.pv
        self.cmt = round(self.ct/self.q, 3) #esto se quita en la segunda vuelta
        self.cmv = round(self.cvt/self.q, 3)
        self.cmf = round(self.cft/self.q, 3)
        self.it = self.q * self.pv
        self.im = self.pv
        self.bop = self.it - self.ct
        self.formato = f"{'Produccion':<10} {'Costo_ft':<10} {'Costo_vt':<10} {'costo_t':<10} {'Costo_mt':<10} {'Costo_mv':<10} {'Costo_mf':<10} {'Costo_mar':<10} {'Ingreso_t':<10} {'ingreso_m':<10} {'Beneficios o perdidas':<15} \n"
        self.formato += (f"{self.q: 5} {self.cft: 10} {self.cvt: 10} {self.ct: 10} {self.cmt: 10} {self.cmv: 10} {self.cmf: 10} {self.cm: 10} {self.it: 10} {self.im: 10} {self.bop: 10}\n")
        return self.formato

