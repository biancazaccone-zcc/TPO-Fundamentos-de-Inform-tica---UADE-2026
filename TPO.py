import random

# ---------------------------------------- SUBFUNCIONES ---------------------------------------------------------------------------

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
    mostrar_menu()
    accion = int(input("Accion a realizar: "))
    while accion < 1 or accion > 5:        #Solo se permite realizar una accion entre las mostradas
        print("La accion no está entre las opciones, por favor elegir una mostrada en el menú.")   
        mostrar_menu()
        accion = int(input("Accion a realizar: "))
    return accion

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

def pedir_nombre(matriz):

    nombre = str(input("Nombre del pokémon: "))
    while not nombre.strip():                # Se revisa que el nombre tenga contenido y no sea solo una entrada vacía
        print("El pokémon debe tener nombre.")
        nombre = str(input("Nombre: "))
    for pokemon in matriz:
        while pokemon[0] == nombre:
            print("Ya hay un pokémon con este nombre, elija otro")
            nombre = str(input("Nombre del pokémon: "))

    return nombre

def pedir_tipo(matriz):
    tipos_posibles = ("fuego", "agua", "planta", "electrico", "psiquico", "lucha", "roca", "fantasma", "dragon", "normal")

    tipo = str(input("Tipo elemental (para valor aleatorio escribir ¨-1¨): "))
    tipo.lower()

    if tipo == "-1":
        tipo = random.choice(tipos_posibles)

    else:
        while tipo not in tipos_posibles:
            print("El tipo no existe.")
            mostrar_tipos()
            tipo = str(input("Tipo elemental: "))
            tipo.lower()

    return tipo

def pedir_nivel(matriz):

    nivel = int(input("Nivel actual (para valor aleatorio escribir ¨-1¨): "))
    
    if nivel == -1:
        nivel = random.randint(1, 100)

    else:
        while nivel < 1 or nivel > 100:
            print("El nivel ingresado no es posible, debe estar entre 1 y 100.")
            nivel = int(input("Nivel actual: "))

    return nivel

def pedir_pc(matriz):

    pc = int(input("Puntos de combate (para valor aleatorio escribir ¨-1¨): "))

    if pc == -1:
        pc = random.randint(1, 6000)

    else:
        while pc < 0:
            print("Los puntos de combate no pueden ser negativos, ingresar correctamente.")
            pc = int(input("Puntos de combate: "))

    return pc

def pedir_nombre_entrenador(matriz):

    entrenador = str(input("Entrenador: "))
    while not entrenador.strip():
        print("El entrenador debe tener nombre.")
        entrenador = str(input("Entrenador: "))

    return entrenador

def pedir_victorias(matriz):

    victorias = int(input("Cantidad de batallas ganadas (para valor aleatorio escribir ¨-1¨): "))
    
    if victorias == -1:
        victorias = random.randint(0, 5000)

    else:
        while victorias < 0:
            print("El numero de victorias es imposible, ingresar correctamente.")
            victorias = int(input("Cantidad de batallas ganadas: "))

    return victorias

def pedir_estado(matriz):
    estados_posibles = ("disponible", "entrenamiento", "lesionado", "liberado")

    estado = str(input("Estado actual (para valor aleatorio escribir ¨-1¨): "))
    estado.lower()

    if estado == "-1":
        estado = random.choice(estados_posibles)

    else:
        while estado not in estados_posibles:
            print("El estado no existe")
            mostrar_estados()
            estado = str(input("Estado actual: "))
            estado.lower()
    return estado

# ---------------------------------------- SUBFUNCIONES ---------------------------------------------------------------------------
# Todas las subfunciones fueron hechas por Héctor Navarro

# ---------------------------------------- FUNCIONES ---------------------------------------------------------------------------

def agregarPKMN(matriz):
    
    # Se pide NOMBRE
    nombre = pedir_nombre(matriz)

    # Se pide TIPO
    tipo = pedir_tipo(matriz)

    # Se pide NIVEL
    nivel = pedir_nivel(matriz)

    # Se pide PUNTOS DE COMBATE
    pc = pedir_pc(matriz)

    # Se pide NOMBRE DEL ENTRENADOR
    entrenador = pedir_nombre_entrenador(matriz)

    # Se pide CANTIDAD DE VICTORIAS
    victorias = pedir_victorias(matriz)

    # Se pide ESTADO
    estado = pedir_estado(matriz)

    # Agregamos el pokémon a la matriz de datos
    matriz.append([nombre, tipo, nivel, pc, entrenador, victorias, estado])
    return matriz

def eliminarPKMN(matriz):
    
    eliminables = []
    
    for fila in matriz:
        if fila[6] == "liberado":
            eliminables.append(fila) #revisa toda la matriz, busca los pokemon liberados y los mete en la lista de pokémons a los que se puede eliminar

    if len(eliminables) == 0:
        print("NO hay pokémons eliminables, tienen que estar liberados para realizar esta acción")
        return matriz

    else:
        opciones = []
        print("Lista de opciones:")
        
        for ELIM in eliminables:
            print(ELIM[0])
            opciones.append(ELIM[0])
        print("Ninguno")
        opciones.append("Ninguno")
            
        accion = str(input("Ingresar nombre de pokémon a eliminar: "))
        while accion not in opciones:
            print("Esa acción no es posible")
            accion = str(input("Ingresar nombre de pokémon a eliminar: "))

        if accion == "Ninguno":
            return matriz
        else:
            for pokemon in matriz[1:]:
                if pokemon[0] == accion:
                    matriz.remove(pokemon)
            return matriz

def verPKMN(matriz):         # Esta sección fue hecha con ia para mostra el informe de pokémons más estéticamente, el método que usó la profesora en clase solo funciona con enteros, este funciona mezclando tipos de datos,
                             # se podría hacer de una manera más simple y que se haya visto en clase pero el reporte se vería menos ordenado.
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

def modificarPKMN(matriz):
    opciones_pokemon = []
    
    print("Las opciones para modificar son las siguientes:")
    print(" ")
    verPKMN(matriz)
    print("Ninguno")

    for fila in matriz[1:]:
        opciones_pokemon.append(fila[0])
        opciones_pokemon.append("Ninguno")
    
    pokemon = str(input("Ingresar nombre del pokémon a modificar o ¨Ninguno¨ para cancelar: "))

    while pokemon not in opciones_pokemon:
            print("la opción elegida no existe")
            print(" ")
            pokemon = str(input("Ingresar nombre del pokémon a modificar o ¨Ninguno¨ para cancelar: "))

    if pokemon == "Ninguno":
        return matriz

    else:

        for fila in matriz[1:]:
            if fila[0] == pokemon:
                matriz.remove(fila)
                print("Ingresar los nuevos datos del pokemon")
                print(" ")
                matriz = agregarPKMN(matriz)

                return matriz

# ---------------------------------------- FUNCIONES ---------------------------------------------------------------------------
# La función agregarPKMN fue hecha por Carlos Wang y Héctor Navarro
# La función EliminarPKMN fue hecha por Bianca Zaccone y Héctor Navarro
# El resto de las funciones fueron hechas por Héctor Navarro

def main():
    matriz = [["Pokemon", "Tipo", "Nivel", "Puntos de combate", "Entrenador/a", "Batallas ganadas", "Estado"]]     #definimos los encabezados de la matriz

    print("Bienvenido, elija una accion:")
    accion = pedir_accion()        #Se pide una accion entre la 1 y la 5

    while accion != 5:
        if accion == 1:
            matriz = agregarPKMN(matriz)
            accion = pedir_accion()

        elif accion == 2:
            matriz = eliminarPKMN(matriz)
            accion = pedir_accion()

        else:
            if accion == 3:
                matriz = modificarPKMN(matriz)
                accion = pedir_accion()

            else:
                verPKMN(matriz)
                accion = pedir_accion()

    print("¡Hasta la próxima!")
                
main()
