import unittest

from raiz_cuadrada import parte_entera_raiz

class TestStringMethods(unittest.TestCase):

    def test_raiz_de_10(self):
      result = parte_entera_raiz(10)
      print(f"resutl: {result}")
      self.assertEqual(result, 3)
    
    def test_raiz_exacta_25(self):
      result = parte_entera_raiz(25)
      print(f"resutl: {result}")
      self.assertEqual(result, 5)
    
    def test_raiz_exacta_100(self):
      result = parte_entera_raiz(100)
      print(f"resutl: {result}")
      self.assertEqual(result, 10)
    
    def test_raiz_120(self):
      result = parte_entera_raiz(120)
      print(f"resutl: {result}")
      self.assertEqual(result, 10)
    
    def test_raiz_exacta_4(self):
      result = parte_entera_raiz(4)
      print(f"resutl: {result}")
      self.assertEqual(result, 2)

    def test_raiz_exacta_1(self):
      result = parte_entera_raiz(1)
      print(f"resutl: {result}")
      self.assertEqual(result, 1)
    
    def test_raiz_exacta_34523453(self):
      result = parte_entera_raiz(34523453)
      print(f"resutl: {result}")
      self.assertEqual(result, 5875)



if __name__ == '__main__':
    unittest.main()