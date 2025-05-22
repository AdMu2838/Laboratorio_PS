saldo = 1000.0

def mostrar_menu():
    print("\n--- Menú Cajero Automático ---")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")

def consultar_saldo():
    print(f"Tu saldo actual es: S/.{saldo:.2f}")

def depositar():
    global saldo
    try:
        monto = float(input("Ingresa el monto a depositar: S/."))
        if monto > 0:
            saldo += monto
            print(f"Has depositado S/.{monto:.2f}. Nuevo saldo: S/.{saldo:.2f}")
        else:
            print("El monto debe ser mayor que cero.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def retirar():
    global saldo
    try:
        monto = float(input("Ingresa el monto a retirar: S/."))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Has retirado S/.{monto:.2f}. Nuevo saldo: S/.{saldo:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def main():
    print("Bienvenido al Cajero Automático")
    print("Tu saldo inicial es: S/.1000.00")

    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            consultar_saldo()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()