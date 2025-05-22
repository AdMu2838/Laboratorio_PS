def validar_cantidad(entrada_cantidad):
    """
    Valida la cantidad de números que el usuario desea ingresar.

    Args:
        entrada_cantidad (str): Entrada del usuario para la cantidad de números.

    Returns:
        int o str: Devuelve la cantidad si es válida, o un mensaje de error si no lo es.
    """
    if entrada_cantidad is None:
        return "Error: falta ingresar la cantidad de números"
    if entrada_cantidad.strip() == "":
        return "Error: por favor ingrese un número válido"
    try:
        cantidad = int(entrada_cantidad)
    except ValueError:
        return "Error: por favor ingrese un número válido"
    if cantidad <= 0:
        return "Cantidad inválida: el número ingresado debe ser > 0"
    return cantidad

def ingresar_numeros(cantidad):
    """
    Solicita al usuario ingresar la cantidad indicada de números enteros.

    Args:
        cantidad (int): Número de valores a ingresar.

    Returns:
        list[int]: Lista con los números enteros ingresados.
    """
    numeros = []
    i = 0
    while i < cantidad:
        entrada = input(f"Ingrese un número entero para la posición {i + 1}: ").strip()
        if entrada == "":
            print(f"\nIngreso vacío no permitido en posición {i + 1}.")
            continue
        try:
            numero = int(entrada)
            numeros.append(numero)
            i += 1
        except ValueError:
            print(f"\nIngreso inválido en la posición {i + 1}. Debe ser un número entero.")
    return numeros

def clasificar_pares_impares(numeros):
    """
    Clasifica cada número como par o impar.

    Args:
        numeros (list[int]): Lista de números enteros.

    Returns:
        list[str]: Lista de resultados indicando si cada número es par o impar.
    """
    resultados = []
    for numero in numeros:
        tipo = "par" if numero % 2 == 0 else "impar"
        resultados.append(f"El número {numero} es {tipo}")
    return resultados

def main():
    entrada = input("¿Cuántos números desea ingresar? ")
    cantidad = validar_cantidad(entrada)
    if isinstance(cantidad, str):
        print(cantidad)
        return
    numeros = ingresar_numeros(cantidad)
    print("\nResultados:")
    for resultado in clasificar_pares_impares(numeros):
        print(resultado)

if __name__ == "__main__":
    main()