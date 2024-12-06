import random

# Diccionario para almacenar los tickets
tickets = {}

def alta_ticket():
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese el sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Describa el problema: ")

    numero_ticket = random.randint(1000, 9999)
    tickets[numero_ticket] = {
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "problema": problema
    }

    print("\nTicket generado:")
    print(f"Numero de Ticket: {numero_ticket}")
    print(f"Nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Problema: {problema}")
    print("Por favor, recuerde su número de ticket.\n")

def leer_ticket():
    numero_ticket = int(input("Ingrese el número de ticket: "))
    if numero_ticket in tickets:
        ticket = tickets[numero_ticket]
        print("\nTicket encontrado:")
        print(f"Numero de Ticket: {numero_ticket}")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Problema: {ticket['problema']}\n")
    else:
        print("Ticket no encontrado.\n")

def menu():
    while True:
        print("Hola bienvenido al sistema de tickets:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_ticket()
            while True:
                otra = input("¿Desea crear otro ticket? (s/n): ")
                if otra.lower() == 's':
                    alta_ticket()
                elif otra.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == "2":
            leer_ticket()
            while True:
                otra = input("¿Desea leer otro ticket? (s/n): ")
                if otra.lower() == 's':
                    leer_ticket()
                elif otra.lower() == 'n':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == "3":
            confirmacion = input("¿Está seguro que desea salir? (s/n): ")
            if confirmacion.lower() == 's':
                print("Saliendo del programa...")
                break
            else:
                print("Cancelado. Regresando al menú principal.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
