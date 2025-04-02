
# Definir nodos con sus equivalencias numéricas
nodes = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Definir las aristas con pesos basados en la suma de equivalencias
edges = [
    ('a', 'b', nodes['a'] + nodes['b']),
    ('a', 'f', nodes['a'] + nodes['f']),
    ('a', 'c', nodes['a'] + nodes['c']),
    ('b', 'f', nodes['b'] + nodes['f']),
    ('b', 'e', nodes['b'] + nodes['e']),
    ('b', 'c', nodes['b'] + nodes['c']),
    ('c', 'e', nodes['c'] + nodes['e']),
    ('c', 'd', nodes['c'] + nodes['d']),
    ('d', 'e', nodes['d'] + nodes['e']),
    ('e', 'f', nodes['e'] + nodes['f'])
]

def kruskal_mst(edges):
    # Ordenar las aristas por peso
    edges.sort(key=lambda x: x[2])
    mst = []
    uf = {node: node for node in nodes}  # Estructura de unión-búsqueda
    size = {node: 1 for node in nodes}  # Tamaño de cada conjunto

    def find(n):
        if uf[n] != n:
            uf[n] = find(uf[n])
        return uf[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 != root2:
            if size[root1] > size[root2]:
                uf[root2] = root1
                size[root1] += size[root2]
            else:
                uf[root1] = root2
                size[root2] += size[root1]

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
        if len(mst) == len(nodes) - 1:  # Detener cuando tengamos V-1 aristas
            break

    return mst

# Calcular el árbol de mínima expansión
mst_edges = kruskal_mst(edges)

# Imprimir las aristas del árbol de mínima expansión
print("Aristas del árbol de mínima expansión:")
for u, v, w in mst_edges:
    print(f"{u} - {v} : {w}")


# el segundo grafo es un grafo dirigido, por lo que no es aplicable el algoritmo de kruskal
