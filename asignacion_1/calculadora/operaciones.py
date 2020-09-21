"""
--Archivo operaciones.py--
En esta seccion se encuentra la parte de operaciones matematicas 
auxiliada por la libreria math, la cual esta divido por dos 
clases (Datos, Operaciones) y sus respectivas funciones, de igual 
manera, tambien recive dos paremetros (numero1 y numero2) que son 
enviados por el archivo main.py 

"""

import math

class Datos():

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

class Operaciones(Datos):

    def suma(self):
        self.resultado = self.numero1 + self.numero2

        return self.resultado
    
    def resta(self):
        self.resultado = self.numero1 - self.numero2

        return self.resultado
    
    def multiplicacion(self):
        self.resultado = self.numero1 * self.numero2
        
        return self.resultado
    
    def division(self):
        if self.numero1 == 0 or self.numero2 == 0:
            self.resultado = "No se puede realizar una division entre 0!"
        else:
            self.resultado = self.numero1 / self.numero2           

        return self.resultado

    def potencia(self):
        self.resultado = pow(self.numero1, self.numero2)

        return self.resultado

    def porcentaje(self):
        self.resultado = (self.numero1 * (self.numero2 / 100))

        return self.resultado

    def raizCuadrada(self):
        self.resultado = f"\n √{self.numero1} = {math.sqrt(self.numero1)}"
        self.resultado += f"\n √{self.numero2} = {math.sqrt(self.numero2)}"

        return self.resultado
    
    def factorial(self):
        self.resultado = f"\n {self.numero1}! = {math.factorial(self.numero1)}"
        self.resultado += f"\n {self.numero2}! = {math.factorial(self.numero2)}"

        return self.resultado





