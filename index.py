from Clases import Costos

niveles = int(input("¿Cuantos niveles de produccion desea registrar? "))
costo_fijo = int(input("¿Cual fue el costo fijo? "))
nivel = 0
while nivel <= niveles:
    costo_total = int(input(f"Introduce el costo total del nivel de produccion numero {nivel}: "))
    objeto = Costos(nivel, costo_total, costo_fijo)
    variable = objeto.costo_variable()
    medio_total = objeto.medio_total()
    print(f"Costo variable: {variable}")
    print(f"Costo medio total: {medio_total}")
    nivel = nivel + 1 
 



