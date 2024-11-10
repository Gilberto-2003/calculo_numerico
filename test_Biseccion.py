import unittest
import math
from Interfaz_biseccion import biseccion, funcion 

class TestBiseccion(unittest.TestCase):

    def test_biseccion_raiz(self):
        raiz, error, _ = biseccion(funcion, 0, 2, 1e-6)
        self.assertIsNotNone(raiz)
        self.assertTrue(abs(funcion(raiz)) < 1e-6)

    def test_biseccion_sin_raiz(self):
        raiz, error, _ = biseccion(funcion, 2, 2, 1e-6)
        self.assertIsNone(raiz)
        self.assertIsNone(error)

if __name__ == '__main__':
    unittest.main()


