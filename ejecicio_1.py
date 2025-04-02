from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, list):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, list)
 
        # Push current vertex to stack which stores result
        list.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        list = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, list)
 
        # Print contents of the stack
        print(list[::-1])  # return list in reverse order

'''
los grafos 1 es un grafo no dirigido, por lo que el ordenamiento
topologico no es aplicable, el grafo 2 es un grafo dirigido, pero posee ciclos,
por lo que el ordenamiento topologico no es aplicable, el grafo 3 es un grafo dirigido aciclico
y dirigido, por lo que el ordenamiento topologico es aplicable.

'''


print("Ordenamiento Topológico para el Grafo 3 (Letras - a, b, g, k, m, s, t):")
# Grafo 3: Nodos a, b, g, k, m, s, t
# Mapeo: a: 0, b: 1, g: 2, k: 3, m: 4, s: 5, t: 6
grafo3 = Graph(7)
grafo3.addEdge(0, 1) # b -> m
grafo3.addEdge(1, 4) # a -> b
grafo3.addEdge(1, 6) # a -> s
grafo3.addEdge(6, 2) # t -> g
grafo3.addEdge(6, 3) # t -> k
grafo3.addEdge(2, 5) # g -> s
grafo3.topologicalSort()