"""
Este programa calcula el área de un rectángulo a partir de su base y altura.
"""
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Args:
        base: Longitud de la base (número entero o decimal).
        altura: Longitud de la altura (número entero o decimal).
    Returns:
        El área calculada del rectángulo.
    """
    # Verifica que son float
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        return None

    # Verificar que las dimensiones sean positivas
    if base <= 0 or altura <= 0:
        return None

    return base * altura

# --- Programa Principal ---
def main():
    print("Calculadora de área de rectángulo")
    print("Ingrese las dimensiones del rectángulo:")

    try:
        # Leer las entradas del usuario y convertirlas a float (para aceptar decimales)
        b = float(input("Base: "))
        h = float(input("Altura: "))

        # Calcular el área
        area = calcular_area_rectangulo(b, h)

        # Mostrar resultados
        if area is not None:
            print(f"\nResultados:\nBase: {b}\nAltura: {h}\nÁrea del rectángulo: {area}")
        else:
            print("\nError: La base y la altura deben ser valores positivos.")

    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        print("\nError: Por favor, ingrese números válidos para la base y la altura.")


if __name__ == "__main__":
    main()