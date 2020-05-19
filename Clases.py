class Costos:
    def __init__ (self, nivel, costo_total, precio, costo_fijo):
        self.__nivel = nivel
        self.__costo_total = costo_total
        self.__precio = precio
        self.__costo_fijo = costo_fijo
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def costo_total(self):
        return self.__costo_total
    
    @property
    def precio(self):
        return self.__precio

    @property
    def costo_fijo(self):
        return self.__costo_fijo

    @nivel.setter
    def nivel(self,valor1):
        self.__nivel = valor1

    @costo_total.setter
    def costo_total(self,valor1):
        self.__costo_total = valor1

    @precio.setter
    def precio(self,valor1):
        self.__precio = valor1

    @costo_total.setter
    def costo_fijo(self,valor1):
        self.__costo_fijo = valor1

    def costo_variable (costo_total, costo_variable):
        resultado = self.__costo_total - self.__costo_fijo