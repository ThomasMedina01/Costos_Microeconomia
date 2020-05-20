import sys
from Formulas import Tabla, pedirNumeroEntero, pedircosto, pedirprecio, pedirOpcion
print("♣-♦-" * 33)
print("SISTEMA DE CALCULO DE COSTOS DE PRODUCCION")
print("♣-♦-" * 33)
while True:
    valor1 = pedirNumeroEntero()
    valor2 = pedircosto()
    valor3 = pedirprecio()
    print("♣-♦-" * 33)
    prueba = Tabla(0, valor2, valor3, 0, 0)
    print(prueba.vertablainicial())
    print("♣-♦-" * 33)
    valor4 = valor2
    valor5 = valor2
    for a in range(1, valor1):
        valor4 = valor2
        valor2 = float(input("Escriba su costo total: "))
        prueba = Tabla(a, valor2, valor3, valor4, valor5)
        print(prueba.vertablafinal())
        print("♣-♦-" * 33)
        valor4 = valor3
    opcion = pedirOpcion()
    if opcion ==0: 
        print("♠♠♠♠♠ Ejecucion Finalizada ♠♠♠♠♠")
        sys.exit()
    





        
   



#print(prueba.vertablainicial())
 



