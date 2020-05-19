class Costos:
    def __init__ (self, nivel, costo_total, costo_fijo):
        self.__nivel = nivel
        self.__costo_total = costo_total
        self.__costo_fijo = costo_fijo
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def costo_total(self):
        return self.__costo_total

    @property
    def costo_fijo(self):
        return self.__costo_fijo

    @nivel.setter
    def nivel(self,valor1):
        self.__nivel = valor1

    @costo_total.setter
    def costo_total(self,valor1):
        self.__costo_total = valor1

    @costo_fijo.setter
    def costo_fijo(self,valor1):
        self.__costo_fijo = valor1

    def costo_variable (self):
        return self.__costo_total - self.__costo_fijo
    
    def medio_total (self):
        if self.__nivel == 0:
            return 0
        return round (self.__costo_total / self.__nivel, 2)
    
    
