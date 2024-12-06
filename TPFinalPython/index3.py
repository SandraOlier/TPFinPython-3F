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

def ta_te_ti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    movimientos = 0

    while movimientos < 9:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingrese la fila (0, 1, 2): "))
        col = int(input(f"Jugador {jugador_actual}, ingrese la columna (0, 1, 2): "))

        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador_actual
            movimientos += 1

            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador_actual} gana!")
                return

            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Celda ocupada, intente de nuevo.")

    imprimir_tablero(tablero)
    print("¡Es un empate!")

if __name__ == "__main__":
    ta_te_ti()
