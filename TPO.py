def crearMatriz():
    for f in range (filas):
        matriz.append([])
        
def agregarPKMN():
    for c in range

def mostrar_menu():
    print("")
    print("1. Registrar Pokémon")
    print("2. Eliminar Pokémon")
    print("3. Modificar Pokémon")
    print("4. Ver Pokémons")
    print("5. Salir")
    print("")

def main():
    print("Bienvenido, elija una accion:")
    
    mostrar_menu()
    accion = int(input("Accion a realizar: "))
    while accion < 1 or accion > 5:        #Solo se permite realiza una accion entre las mostradas
        print("La accion no está entre las opciones, por favor elegir una mostrada en el menú.")   
        mostrar_menu()
        accion = int(input("Accion a realizar: "))

    matriz=[["Pokemon", "Tipo", "Nivel", "Puntos de combate", "Entrenador/a", "Batallas ganadas", "Estado"]]     #definimos los encabezados de la matriz
    filas=7

main()
