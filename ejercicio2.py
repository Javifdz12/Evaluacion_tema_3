import numpy as np
class ejercicio2:
    def __init__(self,matriz):
        self.matriz = matriz
    def regla_sarrus_iterativa(self):
        det=self.matriz[0][0]*self.matriz[1][1]*self.matriz[2][2]+self.matriz[1][0]*self.matriz[2][1]*self.matriz[0][2]+self.matriz[0][1]*self.matriz[1][2]*self.matriz[2][0]-(self.matriz[0][2]*self.matriz[1][1]*self.matriz[2][0]+self.matriz[2][1]*self.matriz[1][2]*self.matriz[0][0]+self.matriz[0][1]*self.matriz[1][0]*self.matriz[2][2])
        return det
    def regla_sarrus_recursiva(self):
        det=np.linalg.det(self.matriz)
        return det
    def ejecutar(self):
        print(self.regla_sarrus_iterativa())
        print(self.regla_sarrus_recursiva())


