class Tabla():
    def __init__(self, q, ct, pv, ctan, cft):
        self.q = q
        self.ct = ct
        self.pv = pv
        self.ctan = ctan
        self.cft = cft

    def vertablainicial(self):
        self.cft = self.ct #solo funciona para la primer fila
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
        self.cmt = round(self.ct/self.q, 3) #Codigo despues de la primera vuelta
        self.cmv = round(self.cvt/self.q, 3)
        self.cmf = round(self.cft/self.q, 3)
        self.it = self.q * self.pv
        self.im = self.pv
        self.bop = self.it - self.ct
        self.formato = ""
        self.formato += (f"{self.q: 5} {self.cft: 10} {self.cvt: 10} {self.ct: 10} {self.cmt: 10} {self.cmv: 10} {self.cmf: 10} {self.cm: 10} {self.it: 10} {self.im: 10} {self.bop: 10}\n")
        return self.formato

opcion = int(input("1.-tabla normal \n2.-tabla para el examen \n"))

if opcion == 1:
    while True:
        valor1 = input("Escriba su la cantidad producida: ")
        if valor1.isdigit():
            valor1 = int(valor1)
            break
        else:
            print("Valor incorrecto intente de nuevo")

    while True:    
        valor2 = input("Escriba su 1° costo total: ")
        if valor2.isdigit():
            valor2 = float(valor2)
            break
        else:
            print("Valor incorrecto intente de nuevo")

    while True:
        valor3 = input("Escriba su precio de venta: ")
        if valor3.isdigit():
            valor3 = float(valor3)
            break
        else:
            print("Valor incorrecto intente de nuevo")

    tabulacion = open("tabla.txt", "w")
    prueba = Tabla(0, valor2, valor3, 0, 0)
    print(prueba.vertablainicial())
    tabulacion.write('%s'%prueba.vertablainicial())

    valor4 = valor2
    valor5 = valor2

    for a in range(1, valor1):
        valor4 = valor2
        while True:    
            valor2 = input(f"Escriba su {a+1}° costo total: ")
            if valor2.isdigit():
                valor2 = float(valor2)
                break
            else:
                print("Valor incorrecto intente de nuevo")
        
        prueba = Tabla(a, valor2, valor3, valor4, valor5)
        print(prueba.vertablafinal())
        tabulacion.write('%s'%prueba.vertablafinal())
        valor4 = valor3

    tabulacion.close()

if opcion == 2:
    def tabular(q, p, ct, ctan, itan,it):
        cm = ct - ctan
        cmt = round(ct / q, 3)
        im = it - itan
        bop = it - ct
        formato = ""
        formato += (f"{q}, {p}, {ct}, {cm}, {cmt}, {it}, {im}, {bop}")
        return formato


    q = int(input("Escriba su cantidad producida: "))
    p = int(input("Escriba su precio de venta: "))
    ct = int(input("Escriba su costo total: "))
    ctn = 0
    itan = 0
    it = p
    tabla = tabular(1, p, ct, ctn, itan, it)
    print(tabla)
    for a in range(1, q+1):
        ctn = ct
        itan = it
        p = int(input("Escriba su precio de venta: "))
        ct = int(input("Escriba su costo total: "))
        n = a + 1
        it = p*n
        tabla = tabular(1, p, ct, ctn, itan, it)
        print(tabla)
