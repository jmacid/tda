# Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. Indicar y justificar la complejidad.
def elemento_desordenado(arr):
    return elemento_desordenado_half(arr)

def elemento_desordenado2(arr):
    return elemento_desordenado_i_f(arr, 0, 1)

def elemento_desordenado_i_f(arr, i, f):
    if arr[i] < arr[f]:
        return elemento_desordenado_i_f(arr, i + 1, f + 1)
    else:
        return arr[i] 


def elemento_desordenado_half(arr):
    if len(arr) == 2:
        return None if arr[0] < arr[1] else arr[0]
    if len(arr) == 1:
        return None
    
    half = len(arr) // 2
    if arr[half -1] > arr[half]:
        return arr[half -1]

    left =  elemento_desordenado_half(arr[half:])
    right = elemento_desordenado_half(arr[:half])

    return left if left != None else right


arreglo_un_poco_desordenado = [1, 2, 5, 3, 8, 10]
value = elemento_desordenado(arreglo_un_poco_desordenado)
print(value)

# value = elemento_desordenado([3, 2])
# print(value)