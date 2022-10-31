import numpy as np
import copy
class ejercicio2:
    def __init__(self,matriz):
        self.matriz = matriz
    def regla_sarrus_iterativa(self):
        det=self.matriz[0][0]*self.matriz[1][1]*self.matriz[2][2]+self.matriz[1][0]*self.matriz[2][1]*self.matriz[0][2]+self.matriz[0][1]*self.matriz[1][2]*self.matriz[2][0]-(self.matriz[0][2]*self.matriz[1][1]*self.matriz[2][0]+self.matriz[2][1]*self.matriz[1][2]*self.matriz[0][0]+self.matriz[0][1]*self.matriz[1][0]*self.matriz[2][2])
        return det
    def regla_sarrus_recursiva(self):
        suma=0
        for i in range(len(self.matriz)): # Itero sobre las columnas
            aux = copy.deepcopy(self.matriz) # Duplico la matriz para no modificar la original y poder hacer los cálculos bien 
            aux.remove(self.matriz[0]) #Elimino la primera fila
            for j in range(len(aux)): #Me muevo por las filas restantes 
                #Creo submatrices sin tener en cuenta la columna actual pero sí la fila
                aux[j] = aux[j][0:i] + aux[j][i+1:]
            #Calculo los determinante de estas submatrices recursivamente y los sumo al total
            suma += (-1) ** (i % 2) * self.matriz[0][i] * self.regla_sarrus_recursiva(aux)
        return suma
    def ejecutar(self):
        print(self.regla_sarrus_iterativa())
        print(self.regla_sarrus_recursiva())


