import unittest

from mas_de_la_mitad import mas_de_la_mitad

class TestStringMethods(unittest.TestCase):

    def test_un_solo_elemento(self):
      result = mas_de_la_mitad([1])
      print(f"resutl: {result}")
      self.assertTrue(result)
    
    def test_dos_elementos(self):
      result = mas_de_la_mitad([1, 1])
      print(f"resutl: {result}")
      self.assertTrue(result)
    
    def test_dos_elementos_distitntos(self):
      result = mas_de_la_mitad([1, 0])
      print(f"resutl: {result}")
      self.assertFalse(result)
    
    def test_tres_elementos_distitntos(self):
      result = mas_de_la_mitad([1, 0, 2])
      print(f"resutl: {result}")
      self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()