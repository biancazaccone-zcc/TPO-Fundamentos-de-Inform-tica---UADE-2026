import FUNCIONES.py

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
