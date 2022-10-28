def crear_list(n):
    list=[]
    for i in range(1,n+1):
        list.append(i)
    return list
class plataforma:
    def __init__(self,aguja1,aguja2,aguja3):
        self.aguja1 =aguja1
        self.aguja2 =aguja2
        self.aguja3 =aguja3
    def mover_disco(self,agujax,agujay):
        d=len(agujax)
        agujay.append(agujax[len(agujax)-1])
        print(f'Se ha movido disco {agujax[d-1]}')
        agujax.remove(agujax[len(agujax)-1])

    def mover_discos(self,agujax,agujay):
        while len(agujay)<=73:
            self.mover_disco(agujax,agujay)

class ejercicio1:
    def __init__(self,plataforma):
        self.plataforma = plataforma
    def ejecutar(self):
        self.plataforma.mover_discos(self.plataforma.aguja1,self.plataforma.aguja2)
        self.plataforma.mover_discos(self.plataforma.aguja2,self.plataforma.aguja3)

plat=plataforma(crear_list(74),[],[])
ej1=ejercicio1(plat)
ej1.ejecutar()




