import unittest

from unos_y_ceros import indice_primer_cero

class TestStringMethods(unittest.TestCase):

    def test_sin_ceros(self):
      unos_y_ceros = [1, 1, 1]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, -1)

    def test_hay_cero(self):
      unos_y_ceros = [1, 1, 1, 0]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, 3)

    def test_hay_mas_de_un_cero(self):
      unos_y_ceros = [1, 1, 1, 0, 0]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, 3)
    
    def test_hay_un_cero_en_la_primer_mitad(self):
      unos_y_ceros = [1, 0, 0, 0]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, 1)

    def test_sin_ceros2(self):
      unos_y_ceros = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, -1)

    def test_hay_un_cero_en_la_segunda_mitad(self):
      unos_y_ceros = [1, 1, 0, 0]
      result = indice_primer_cero(unos_y_ceros)
      self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()