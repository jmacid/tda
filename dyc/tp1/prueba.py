# Definir una función para resolver el problema
def ordenar_batallas(batallas):
    # batallas es una lista de tuplas (t_i, b_i)

    # Calcular la razón (t_i / b_i) para cada batalla
    batallas_ordenadas = sorted(batallas, key=lambda x: x[0] / x[1])

    return batallas_ordenadas

# Función para calcular la suma ponderada de los tiempos de finalización
def calcular_suma_ponderada(batallas):
    batallas_ordenadas = ordenar_batallas(batallas)
    tiempo_final = 0
    suma_ponderada = 0

    # Iterar sobre las batallas en el orden óptimo
    for t_i, b_i in batallas_ordenadas:
        tiempo_final += t_i  # La batalla i termina después del tiempo t_i
        suma_ponderada += b_i * tiempo_final  # Sumar el impacto ponderado de la batalla

    return suma_ponderada

# Ejemplo de uso
# batallas = [(53,100), (61,100), (68,100), (68,100),(86,100), (35,100), (97,100), (58,100), (47,100), (82,100)]  # Cada batalla es (t_i, b_i)
batallas = [ (10,1), (1, 10), (10, 10), (2,2)]

resultado = calcular_suma_ponderada(batallas)
print(f"La suma ponderada de los tiempos de finalización es: {resultado}")


