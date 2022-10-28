import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio3 import ejercicio3,nave
import helpers
import ejercicio4
import ejercicio5


def menu():
    print("========================")
    print(" BIENVENIDO AL MENU ")
    print("========================")
    print("[1] Ejercicio 1 ")
    print("[2] Ejercicio 2 ")
    print("[3] Ejercicio 3 ")
    print("[4] Ejercicio 4 ")
    print("[5] Ejercicio 5 ")
    print("[6] Salir ")
    print("========================")

def iniciar():
    m=[[1,1,1],[1,0,1],[0,1,0]]
    ej2=ejercicio2(m)
    nave1=nave('Halcon milenario',60,10,50)
    nave2=nave('Estrella de la Muerte',20000,2000,5000)
    nave3=nave('AT1',40,3,5)
    nave4=nave('AT2',40,3,5)
    nave5=nave('AT3',40,3,5)
    nave6=nave('AT4',40,3,5)
    lista_naves=[nave1,nave2,nave3,nave4,nave5,nave6]
    ej3=ejercicio3(lista_naves)

    while True:

        menu()
        opcion = int(input("> "))
        helpers.limpiar_pantalla()

        if opcion == 1:
            pass

        if opcion == 2:
            ej2.ejecutar()

        if opcion == 3:
            ej3.ejecutar()

        if opcion==4:
            pass

        if opcion==5:
            pass

        if opcion == 6:
            print("Saliendo...\n")
            break