import random
import string

def generar_contrasena(longitud, tipo):
    if tipo == 1:
        caracteres = string.ascii_letters
    elif tipo == 2:
        caracteres = string.digits
    elif tipo == 3:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def menu_contrasena():
    print("Welcome")
    print("Generador de Contraseñas V0.1\n")
    while True:
        print("Seleccione una de las siguientes opciones:")
        print("1. Generar contraseña solo de letras")
        print("2. Generar contraseña solo de números")
        print("3. Generar contraseña letras, números y caracteres")
        print("0. Salir")
        opcion = int(input("Escriba la opción seleccionada: "))

        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion in [1, 2, 3]:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            contrasena = generar_contrasena(longitud, opcion)
            if contrasena:
                print(f"Contraseña generada: {contrasena}")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_contrasena()
