import unittest
from unittest.mock import patch
from io import StringIO
import cajero  # suponiendo que guardaste tu código en cajero.py

class TestCajero(unittest.TestCase):

    def setUp(self):
        cajero.saldo = 1000.0  # Reiniciar saldo antes de cada test

    @patch('sys.stdout', new_callable=StringIO)
    def test_consultar_saldo(self, mock_stdout):
        cajero.consultar_saldo()
        self.assertIn("Tu saldo actual es: S/.1000.00", mock_stdout.getvalue())

    @patch('builtins.input', return_value='500')
    @patch('sys.stdout', new_callable=StringIO)
    def test_depositar_valido(self, mock_stdout, _):
        cajero.depositar()
        self.assertIn("Has depositado S/.500.00", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1500.0)

    @patch('builtins.input', return_value='-200')
    @patch('sys.stdout', new_callable=StringIO)
    def test_depositar_negativo(self, mock_stdout, _):
        cajero.depositar()
        self.assertIn("El monto debe ser mayor que cero", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1000.0)

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_depositar_invalido(self, mock_stdout, _):
        cajero.depositar()
        self.assertIn("Por favor, ingresa un número válido", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1000.0)

    @patch('builtins.input', return_value='200')
    @patch('sys.stdout', new_callable=StringIO)
    def test_retirar_valido(self, mock_stdout, _):
        cajero.retirar()
        self.assertIn("Has retirado S/.200.00", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 800.0)

    @patch('builtins.input', return_value='2000')
    @patch('sys.stdout', new_callable=StringIO)
    def test_retirar_excede_saldo(self, mock_stdout, _):
        cajero.retirar()
        self.assertIn("Fondos insuficientes", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1000.0)

    @patch('builtins.input', return_value='-100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_retirar_monto_negativo(self, mock_stdout, _):
        cajero.retirar()
        self.assertIn("El monto debe ser mayor que cero", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1000.0)

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_retirar_invalido(self, mock_stdout, _):
        cajero.retirar()
        self.assertIn("Por favor, ingresa un número válido", mock_stdout.getvalue())
        self.assertEqual(cajero.saldo, 1000.0)

    @patch('builtins.input', side_effect=['1', '2', '500', '3', '200', '4'])  # consultar, depositar, retirar y salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_opciones_validas(self, mock_stdout, _):
        cajero.main()
        salida = mock_stdout.getvalue()
        self.assertIn("Tu saldo actual es: S/.1000.00", salida)
        self.assertIn("Has depositado S/.500.00", salida)
        self.assertIn("Has retirado S/.200.00", salida)
        self.assertIn("Gracias por usar el cajero", salida)

    @patch('builtins.input', side_effect=['1', '4'])  # consultar y salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_opcion_1_y_salir(self, mock_stdout, _):
        cajero.main()
        salida = mock_stdout.getvalue()
        self.assertIn("Tu saldo actual es: S/.1000.00", salida)
        self.assertIn("Gracias por usar el cajero", salida)


if __name__ == '__main__':
    unittest.main()
