# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

# Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

def parte_entera_raiz(n):
    if n == 0 or n == 1:
        return n
    # return _parte_entera_raiz(n, n//2)
    return _parte_entera_raiz_binaria(n, 0, n)



def _parte_entera_raiz(n_org, n):
    
    if n*n <= n_org  and n_org < (n + 1)*(n + 1):
        return n
    if  n*n > n_org :
         return _parte_entera_raiz(n_org, n-1)
    else:
         return _parte_entera_raiz(n_org, n+1)
    
def _parte_entera_raiz_binaria(n, i, f):
    if f < i:
        return f
    
    halve = (f + i) // 2
    square = halve * halve

    if square == n:
        return halve
    elif square < n:
        return _parte_entera_raiz_binaria(n, halve + 1, f)
    else:
        return _parte_entera_raiz_binaria(n, i, halve - 1)