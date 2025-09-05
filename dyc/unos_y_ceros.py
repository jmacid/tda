# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.

def indice_primer_cero(arr):
    if arr[0] == 1 and arr[len(arr) - 1] == 1:
        return -1
    result = _indice_primer_cero(arr, 0, len(arr) -1)
    # print(f"result: {result}")
    return result


def _indice_primer_cero(arr, i, f):
    if f - i == 0:
        return -1 if arr[i] == 1 else i
    if len(arr) -1 == i or f - i < 0 :
        return -1
    
    halfway = (i + f) // 2
    if arr[halfway] == 1 and arr[halfway + 1] == 0:
        return halfway + 1
    elif arr[halfway] == 1:
        return _indice_primer_cero(arr, i + halfway, f)
    elif arr[halfway] == 0 and  arr[halfway -1] == 1:
        return halfway
    else:
        return _indice_primer_cero(arr, i, i + halfway)