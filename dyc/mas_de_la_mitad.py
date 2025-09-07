def mas_de_la_mitad(arr):
    conteo = {}
    return _mas_de_la_mitad(arr, conteo, 0, len(arr) - 1)

def _mas_de_la_mitad(arr, conteo, i, f): 
    if f < i:
        return False
    
    medio = (f + i) // 2

    if arr[medio] in conteo:
        conteo[arr[medio]] += 1
    else:
      conteo[arr[medio]] = 1

    if conteo[arr[medio]] > len(arr) // 2:
        return True
    
    return _mas_de_la_mitad(arr, conteo, i, medio - 1) or _mas_de_la_mitad(arr, conteo, medio + 1, f ) 

