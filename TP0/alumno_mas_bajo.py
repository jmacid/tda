class Alumno:
  def __init__(self, nombre: str, altura: float):
    self.nombre = nombre
    self.altura = altura

# 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23
alumnos = [
  Alumno(nombre="alumno 1", altura=1.2),
  Alumno(nombre="alumno 4", altura=1.15),
  Alumno(nombre="alumno 7", altura=1.14),
  Alumno(nombre="alumno 6", altura=1.12),
  Alumno(nombre="alumno 2", altura=1.02),
  Alumno(nombre="alumno 5", altura=0.98),
  Alumno(nombre="alumno 8", altura=1.18),
  Alumno(nombre="alumno 3", altura=1.23),
]


def binary_search(vector, init, end):
  if end == init:
    return end
  else:
    middle = (end + init) // 2
    if vector[middle].altura < vector[middle + 1].altura:
      left = binary_search(vector, init, middle)
      return left
    else:
      right = binary_search(vector, middle + 1, end)
      return right



def indice_mas_bajo(alumnos):                   
    min_height_i = binary_search(alumnos, 0, len(alumnos) - 1)
    # print(f"Altura mas baja: {min_height_i}")
    return min_height_i

def validar_mas_bajo(alumnos, indice):
    return alumnos[indice].altura < alumnos[indice + 1].altura and alumnos[indice].altura < alumnos[indice - 1].altura


indice_mas_bajo(alumnos)
if validar_mas_bajo(alumnos, 1):
  print("Es el mas bajo")
else:
  print("NO es el mas bajo")
