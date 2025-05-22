import unittest
from unittest.mock import patch
from io import StringIO
from rectangulo import calcular_area_rectangulo, main

class TestCalcularAreaRectangulo(unittest.TestCase):

    def test_area_valores_validos_enteros(self):
        self.assertEqual(calcular_area_rectangulo(5, 10), 50)

    def test_area_valores_validos_decimales(self):
        self.assertAlmostEqual(calcular_area_rectangulo(3.5, 2), 7.0)

    def test_base_negativa(self):
        self.assertIsNone(calcular_area_rectangulo(-5, 10))

    def test_altura_negativa(self):
        self.assertIsNone(calcular_area_rectangulo(5, -10))

    def test_base_cero(self):
        self.assertIsNone(calcular_area_rectangulo(0, 4))

    def test_altura_cero(self):
        self.assertIsNone(calcular_area_rectangulo(4, 0))

    def test_valores_no_numericos(self):
        self.assertIsNone(calcular_area_rectangulo("a", 10))
        self.assertIsNone(calcular_area_rectangulo(5, "b"))
        self.assertIsNone(calcular_area_rectangulo("a", "b"))
    def test_valores_extremos(self):
        self.assertEqual(calcular_area_rectangulo(1e6, 1e6), 1e12)
        self.assertEqual(calcular_area_rectangulo(1e-6, 1e-6), 1e-12)


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=["5", "10"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valores_validos_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Área del rectángulo: 50.0", output)

    @patch('builtins.input', side_effect=["abc", "5"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_base_no_numerica(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Por favor, ingrese números válidos para la base y la altura.", output)

    @patch('builtins.input', side_effect=["5", "abc"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_altura_no_numerica(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Por favor, ingrese números válidos para la base y la altura.", output)

    @patch('builtins.input', side_effect=["-5", "10"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_base_negativa_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: La base y la altura deben ser valores positivos.", output)

    @patch('builtins.input', side_effect=["5", "-10"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_altura_negativa_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: La base y la altura deben ser valores positivos.", output)
    
    @patch('builtins.input', side_effect=["0", "4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_base_cero_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: La base y la altura deben ser valores positivos.", output)
    
    @patch('builtins.input', side_effect=["4", "0"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_altura_cero_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: La base y la altura deben ser valores positivos.", output)

    @patch('builtins.input', side_effect=["1e6", "1e6"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valores_extremos_en_main(self, mock_stdout, _):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Área del rectángulo: 1000000000000.0", output)
        

if __name__ == '__main__':
    unittest.main()