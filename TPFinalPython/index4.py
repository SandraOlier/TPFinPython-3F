import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def obtener_movimientos_disponibles(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                movimientos.append((i, j))
    return movimientos

def movimiento_maquina(tablero):
    movimientos = obtener_movimientos_disponibles(tablero)
    return random.choice(movimientos)

def ta_te_ti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    maquina = "O"
    movimientos = 0

    while movimientos < 9:
        imprimir_tablero(tablero)
        if movimientos % 2 == 0:
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            col = int(input("Ingrese la columna (0, 1, 2): "))
            if tablero[fila][col] == " ":
                tablero[fila][col] = jugador
                movimientos += 1
                if verificar_ganador(tablero, jugador):
                    imprimir_tablero(tablero)
                    print("¡Felicidades! ¡Has ganado!")
                    return
            else:
                print("Celda ocupada, intente de nuevo.")
        else:
            fila, col = movimiento_maquina(tablero)
            tablero[fila][col] = maquina
            movimientos += 1
            if verificar_ganador(tablero, maquina):
                imprimir_tablero(tablero)
                print("La máquina ha ganado. ¡Inténtalo de nuevo!")
                return

    imprimir_tablero(tablero)
    print("¡Es un empate!")

if __name__ == "__main__":
    ta_te_ti()
