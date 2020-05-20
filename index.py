from Formulas import Tabla

#prueba = Tabla(0, 20, 22, 0, 0)

valor1 = int(input("¿Cuantos niveles de produccion desea registrar? (Comenzando desde el nivel 0): "))
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
 



