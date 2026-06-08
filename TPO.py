def mostrar_menu():
    print("--------------------------")
    print(" ")
    print("1. Registrar Pokémon")
    print("2. Eliminar Pokémon")
    print("3. Modificar Pokémon")
    print("4. Ver Pokémons")
    print("5. Salir")
    print(" ")
    print("--------------------------")

def pedir_accion():
    global accion
    mostrar_menu()
    accion = int(input("Accion a realizar: "))
    while accion < 1 or accion > 5:        #Solo se permite realizar una accion entre las mostradas
        print("La accion no está entre las opciones, por favor elegir una mostrada en el menú.")   
        mostrar_menu()
        accion = int(input("Accion a realizar: "))

def mostrar_tipos():
    print("Tipos disponibles:")
    print(" ")
    print("· Fuego")
    print("· Agua")
    print("· Planta")
    print("· Electrico")
    print("· Psiquico")
    print("· Lucha")
    print("· Roca")
    print("· Fantasma")
    print("· Dragon")
    print("· Normal")
    print(" ")

def mostrar_estados():
    print("Estados posibles:")
    print(" ")
    print("· Disponible")
    print("· Entrenamiento")
    print("· Lesionado")
    print("· Liberado")
    print(" ")

def agregarPKMN():
    global matriz
    
    tipos_posibles = ("fuego", "agua", "planta", "electrico", "psiquico", "lucha", "roca", "fantasma", "dragon", "normal")
    estados_posibles = ("disponible", "entrenamiento", "lesionado", "liberado")
    
    # Se pide NOMBRE
    nombre = str(input("Nombre: "))
    while not nombre.strip():
        print("El pokémon debe tener nombre.")
        nombre = str(input("Nombre: "))

    # Se pide TIPO
    tipo = str(input("Tipo elemental: "))
    tipo.lower()
    while tipo not in tipos_posibles:
        print("El tipo no existe.")
        mostrar_tipos()
        tipo = str(input("Tipo elemental: "))
        tipo.lower()

    # Se pide NIVEL
    nivel = int(input("Nivel actual: "))
    while nivel < 1 or nivel > 100:
        print("El nivel ingresado no es posible, ingresar correctamente.")
        nivel = int(input("Nivel actual: "))

    # Se pide PUNTOS DE COMBATE
    pc = int(input("Puntos de combate: "))
    while pc < 0:
        print("Los puntos de combate no pueden ser negativos, ingresar correctamente.")
        pc = int(input("Puntos de combate: "))

    # Se pide NOMBRE DEL ENTRENADOR
    entrenador = str(input("Entrenador: "))
    while not entrenador.strip():
        print("El entrenador debe tener nombre.")
        entrenador = str(input("Entrenador: "))

    # Se pide CANTIDAD DE VICTORIAS
    victorias = int(input("Cantidad de batallas ganadas: "))
    while victorias < 0:
        print("El numero de victorias es imposible, ingresar correctamente.")
        victorias = int(input("Cantidad de batallas ganadas: "))

    # Se pide ESTADO
    estado = str(input("Estado actual: "))
    estado.lower()
    while estado not in estados_posibles:
        print("El estado no existe")
        mostrar_estados()
        estado = str(input("Estado actual: "))
        estado.lower()

    # Agregamos el pokémon a la matriz de datos
    matriz.append([nombre, tipo, nivel, pc, entrenador, victorias, estado])

def eliminarPKMN():
    global matriz
    
    eliminables = []
    
    for fila in matriz:
        if fila[6] == "liberado":
            eliminables.append(fila) #revisa toda la matriz, busca los pokemon liberados y los mete en la lista de pokémons a los que se puede eliminar

    if len(eliminables) == 0:
        print("NO hay pokémons eliminables, tienen que estar liberados para realizar esta acción")
        return

    else:
        opciones = {}
        print("Lista de opciones:")
        
        i = 1
        for ELIM in eliminables:
            opciones[i] = ELIM
            print(i,".",ELIM)
            i += 1

        opciones[i] = "Ninguno"
        print(i,"Ninguno")

        accion = int(input("Ingresar pokémon a eliminar: "))
        
        while accion < 0 or accion > i:
            print("La opción no existe.")
            accion = int(input("Ingresar pokémon a eliminar: "))

        if accion == i:        # En caso de elegir la última opción (siempre va a ser "Ninguno") se vuelve al menú principal
            return

        else:
            matriz.remove(opciones[accion])

def modificarPKMN():
    print("en desarrollo")

def verPKMN():        # Esta sección fue hecha con ia para mostra el informe de pokémons más estéticamente, el método que usó la profesora en clase solo funciona con enteros, este funciona mezclando tipos de datos,
    global matriz     # se podría hacer de una manera más simple y que se haya visto en clase pero el reporte se vería menos ordenado.
    
    # Mostramos el informe de pokémons en la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    ancho_maximo = 0
    for f in range(filas):
        for c in range(columnas):
            largo_actual = len(str(matriz[f][c]))
            if largo_actual > ancho_maximo:
                ancho_maximo = largo_actual

    ancho_columna = ancho_maximo + 2

    for f in range(filas):
        for c in range(columnas):
            print(f"{str(matriz[f][c]):>{ancho_columna}}", end="")
        print()

def main():
    global matriz, accion

    matriz = [["Pokemon", "Tipo", "Nivel", "Puntos de combate", "Entrenador/a", "Batallas ganadas", "Estado"]]     #definimos los encabezados de la matriz

    print("Bienvenido, elija una accion:")
    pedir_accion()        #Se pide una accion entre la 1 y la 5

    while accion != 5:
        if accion == 1:
            agregarPKMN()
            pedir_accion()

        elif accion == 2:
            eliminarPKMN()
            pedir_accion()

        else:
            if accion == 3:
                modificarPKMN()
                pedir_accion()

            else:
                verPKMN()
                pedir_accion()

    print("¡Hasta la próxima!")
                
main()
