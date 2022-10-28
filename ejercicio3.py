
class nave:
    def __init__(self,nombre,largo,tripulacion,cantidad_pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidad_pasajeros = cantidad_pasajeros
    def mostrar_informacion(self):
        return f'Nombre:{self.nombre}\nLargo:{self.largo}\nTripulacion:{self.tripulacion}\nCantidad pasajeros:{self.cantidad_pasajeros}'

nave1=nave('Halcon milenario',60,10,50)
nave2=nave('Estrella de la Muerte',20000,2000,5000)
nave3=nave('AT1',40,3,5)
nave4=nave('AT2',40,3,5)
nave5=nave('AT3',40,3,5)
nave6=nave('AT4',40,3,5)
lista_naves=[nave1,nave2,nave3,nave4,nave5,nave6]
class ejercicio3:
    def __init__(self,lista_naves):
        self.naves=lista_naves
    def ordenar_por_pasajeros(self):
        n = len(self.naves)
        for i in range(n):
            derecha = self.naves[i].cantidad_pasajeros
            for j in range(i - 1, -1, -1):
                izquierda = self.naves[j].cantidad_pasajeros
                if derecha > izquierda:
                    self.naves[j + 1].cantidad_pasajeros = izquierda
                    self.naves[j].cantidad_pasajeros = derecha
                    derecha = self.naves[j].cantidad_pasajeros
        return self.naves

    def ordenar_por_tripulacion(self):
        n = len(self.naves)
        for i in range(n):
            derecha = self.naves[i].tripulacion
            for j in range(i - 1, -1, -1):
                izquierda = self.naves[j].tripulacion
                if derecha > izquierda:
                    self.naves[j + 1].tripulacion = izquierda
                    self.naves[j].tripulacion = derecha
                    derecha = self.naves[j].tripulacion
        return self.naves

    def ordenar_por_largo(self):
        n = len(self.naves)
        for i in range(n):
            derecha = self.naves[i].largo
            for j in range(i - 1, -1, -1):
                izquierda = self.naves[j].largo
                if derecha > izquierda:
                    self.naves[j + 1].largo = izquierda
                    self.naves[j].largo = derecha
                    derecha = self.naves[j].largo
        return self.naves

    def naves_mas_pobladas(self):
        list1=self.ordenar_por_pasajeros()
        list2=[]
        for nave in list1:
            while len(list2)<5:
                list2.append(nave)
        else:
            return list2

    def nave_con_mayor_tripulacion(self):
        list=self.ordenar_por_tripulacion()
        return list[0]

    def naves_AT(self):
        list=[]
        for i in self.naves:
            if i.nombre[0]=='A' and i.nombre[1]=='T':
                list.append(i)
        return list

    def naves_min_6_pasajeros(self):
        list=[]
        for i in self.naves:
            if i.cantidad_pasajeros>=6:
                list.append(i)
        return list

    def inf_navegrande_y_navepequeña(self):
        list=self.ordenar_por_largo()
        return f'NAVE GRANDE\n\n{list[0].mostrar_informacion()}\n\nNAVE PEQUEÑA\n\n{list[len(list)-1].mostrar_informacion()}'

    def ejecutar(self):
        print(self.naves[0].mostrar_informacion())
        print(self.naves[1].mostrar_informacion())
        print(self.naves_mas_pobladas())
        print(self.nave_con_mayor_tripulacion())
        print(self.naves_AT())
        print(self.naves_min_6_pasajeros())
        print(self.inf_navegrande_y_navepequeña())






