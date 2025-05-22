import unittest
from unittest.mock import patch
from io import StringIO
from pares import validar_cantidad, clasificar_pares_impares, main

class TestValidarCantidad(unittest.TestCase):

    def test_valido(self):
        self.assertEqual(validar_cantidad("4"), 4)

    def test_none(self):
        self.assertEqual(validar_cantidad(None), "Error: falta ingresar la cantidad de números")

    def test_vacio(self):
        self.assertEqual(validar_cantidad(""), "Error: por favor ingrese un número válido")

    def test_espacio(self):
        self.assertEqual(validar_cantidad("   "), "Error: por favor ingrese un número válido") 

    def test_no_numerico(self):
        self.assertEqual(validar_cantidad("abc"), "Error: por favor ingrese un número válido")

    def test_cero(self):
        self.assertEqual(validar_cantidad("0"), "Cantidad inválida: el número ingresado debe ser > 0")

    def test_negativo(self):
        self.assertEqual(validar_cantidad("-3"), "Cantidad inválida: el número ingresado debe ser > 0")



class TestClasificarParesImpares(unittest.TestCase):

    def test_mezcla_numeros(self):
        numeros = [1, 2, 3, 4]
        esperado = [
            "El número 1 es impar",
            "El número 2 es par",
            "El número 3 es impar",
            "El número 4 es par"
        ]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)

    def test_todos_pares(self):
        numeros = [2, 4, 6]
        esperado = [
            "El número 2 es par",
            "El número 4 es par",
            "El número 6 es par"
        ]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)

    def test_todos_impares(self):
        numeros = [1, 3, 5]
        esperado = [
            "El número 1 es impar",
            "El número 3 es impar",
            "El número 5 es impar"
        ]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)

    def test_vacio(self):
        self.assertEqual(clasificar_pares_impares([]), [])

    def test_un_numero_impar(self):
        numeros = [1]
        esperado = ["El número 1 es impar"]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)

    def test_un_numero_par(self):
        numeros = [8]
        esperado = ["El número 8 es par"]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)

    def test_0(self):
        numeros = [0]
        esperado = ["El número 0 es par"]
        self.assertEqual(clasificar_pares_impares(numeros), esperado)



class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=["", ""])  # cantidad vacía
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_cantidad_vacia(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("Error: por favor ingrese un número válido", salida)

    @patch('builtins.input', side_effect=["abc", ""])  # cantidad no numérica
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_cantidad_no_numerica(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("Error: por favor ingrese un número válido", salida)

    @patch('builtins.input', side_effect=["-2", ""])  # cantidad negativa
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_cantidad_negativa(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("Cantidad inválida", salida)

    @patch('builtins.input', side_effect=["3", "2", "3", "4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valores_validos(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("El número 2 es par", salida)
        self.assertIn("El número 3 es impar", salida)
        self.assertIn("El número 4 es par", salida)

    @patch('builtins.input', side_effect=["2", "", "3", "x", "4"])  # mezcla de errores
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_errores_en_numeros(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("Ingreso vacío no permitido", salida)
        self.assertIn("Ingreso inválido en la posición 2", salida)
        self.assertIn("El número 3 es impar", salida)
        self.assertIn("El número 4 es par", salida)

    @patch('builtins.input', side_effect=["0", ""])  # cantidad cero
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_cantidad_cero(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("Cantidad inválida", salida)

    @patch('builtins.input', side_effect=["1", "0"])  # un número cero
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_un_numero_cero(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("El número 0 es par", salida)

    @patch('builtins.input', side_effect=["1", "1"])  # un número uno
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_un_numero_uno(self, mock_stdout, _):
        main()
        salida = mock_stdout.getvalue()
        self.assertIn("El número 1 es impar", salida)


if __name__ == "__main__":
    unittest.main()
