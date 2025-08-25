import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

grafo = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'D': 1},
    'C': {'A': 1, 'E': 1},
    'D': {'B': 1},
    'E': {'C': 1}
}


def es_bipartito(grafo):
    colores = {}

    for v in grafo.vertices():
        if v not in colores:
            cola = deque()
            cola.append(v)
            colores[v] = 0

            while cola:
                actual = cola.popleft()
                color_actual = colores[actual]
                color_vecino = 1 - color_actual

                for vecino in grafo.adyacentes(actual):
                    if vecino not in colores:
                        colores[vecino] = color_vecino
                        cola.append(vecino)
                    elif colores[vecino] == color_actual:
                        return False
    return True


# Example of a bipartite graph:
# 0 -- 1
# |    |
# 3 -- 2

graph = [
    [1, 3],  # neighbors of 0
    [0, 2],  # neighbors of 1
    [1, 3],  # neighbors of 2
    [0, 2]   # neighbors of 3
]

print(is_bipartite(graph))  # Output: True