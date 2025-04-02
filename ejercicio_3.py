import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vértice \tDistancia desde el Origen")
        for node in range(self.V):
            node_label = chr(65 + node)  # Convierte índice a letra (A=0, B=1, etc.)
            print(f"{node_label} \t\t{dist[node]}")

    def minDistance(self, dist, sptSet):
        min_dist = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min_dist and sptSet[u] == False:
                min_dist = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V  
        dist[src] = 0 
        sptSet = [False] * self.V  

        predecessor = [-1] * self.V

        for count in range(self.V):
            u = self.minDistance(dist, sptSet)
            if u == -1:
                break
                
            sptSet[u] = True

            for v in range(self.V):

                if (self.graph[u][v] > 0 and 
                    sptSet[v] == False and 
                    dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    predecessor[v] = u

        print(f"\nResultados desde el nodo origen {chr(65 + src)}:")
        self.printSolution(dist)

        self.printPaths(src, dist, predecessor)
        
        return dist, predecessor
    
    def printPaths(self, src, dist, predecessor):
        print("\nCaminos más cortos:")
        for i in range(self.V):
            if i != src:
                path = []
                self.getPath(i, predecessor, path)
                if dist[i] == sys.maxsize:
                    print(f"{chr(65 + src)} → {chr(65 + i)}: No alcanzable")
                else:
                    path_str = " → ".join([chr(65 + node) for node in path])
                    print(f"{chr(65 + src)} → {chr(65 + i)} (Distancia: {dist[i]}): {path_str}")
    
    def getPath(self, current, predecessor, path):
        if predecessor[current] == -1:
            path.append(current)
            return
        
        self.getPath(predecessor[current], predecessor, path)
        path.append(current)

def main():
    g = Graph(8)

    g.graph = [
        # A  B  C  D  E  F  G  H
        [0, 3, 5, 2, 0, 0, 0,10],  # A
        [3, 0, 5, 8, 4, 0, 6, 6],  # B
        [5, 5, 0, 0, 1, 7, 9, 0],  # C
        [2, 8, 0, 0, 12, 0, 0, 14],  # D
        [0, 4, 1, 12, 0, 0, 15, 0],  # E
        [0, 0, 7, 0, 0, 0, 0, 9],  # F
        [0, 6, 9, 0, 15, 0, 0, 3],  # G
        [10,6, 0, 14, 0, 9, 3, 0]   # H
    ]

    print("Estructura del grafo (matriz de adyacencia):")
    print("   ", " ".join([f"{chr(65+i):2}" for i in range(g.V)]))
    for i in range(g.V):
        print(f"{chr(65+i):2}", end=" ")
        for j in range(g.V):
            print(f"{g.graph[i][j]:2}", end=" ")
        print()

    start_nodes = range(g.V) 
    for src in start_nodes:
        g.dijkstra(src)
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()