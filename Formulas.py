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
        self.formato = ""
        self.formato += (f"{self.q: 5} {self.cft: 10} {self.cvt: 10} {self.ct: 10} {self.cmt: 10} {self.cmv: 10} {self.cmf: 10} {self.cm: 10} {self.it: 10} {self.im: 10} {self.bop: 10}\n")
        return self.formato

#prueba = Tabla(0, 20, 22, 0, 0)

valor1 = int(input("¿Cuantos niveles de produccion desea registrar? "))
valor2 = float(input("Escriba su costo total: "))
valor3 = float(input("Escriba su precio de venta: "))
prueba = Tabla(0, valor2, valor3, 0, 0)
print(prueba.vertablainicial())
valor4 = valor2
valor5 = valor2
for a in range(1, valor1):
    valor4 = valor2
    valor2 = float(input("Escriba su costo total: "))
    prueba = Tabla(a, valor2, valor3, valor4, valor5)
    print(prueba.vertablafinal())
    valor4 = valor3

#print(prueba.vertablainicial())