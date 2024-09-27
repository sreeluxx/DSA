class Graph:
    def __init__(self, directed=False):
        self.graph = {}  # Dictionary to store the adjacency list
        self.directed = directed  # Boolean flag to indicate if the graph is directed or not

    def addVertex(self, vertex):
        # If the vertex is not already in the graph, add it with an empty adjacency list
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, src, dest):
        # Ensure both source and destination vertices are in the graph
        self.addVertex(src)
        self.addVertex(dest)

        # Add the edge from src to dest
        self.graph[src].append(dest)

        # If the graph is undirected, also add the reverse edge from dest to src
        if not self.directed:
            self.graph[dest].append(src)

    def displayGraph(self):
        # Display the adjacency list of the graph
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def bfs(self,startVertex):
        queue= [startVertex]
        visited={startVertex:True}

        while queue:
         currentVertex= queue.pop(0)
         print(currentVertex,end=' ')

         for neighbor in self.graph[currentVertex]:
            if neighbor not in visited:
                visited[neighbor]=True
                queue.append(neighbor)

    def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end=' ')
            visited[vertex]=True

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
            


    

# Example usage
G = Graph(directed=False)  # Create an undirected graph
G.addEdge('A', 'B')
G.addEdge('A', 'D')
G.addEdge('B', 'C')
G.addEdge('C', 'D')
G.addEdge('B','F')
G.addEdge('D','E')

G.displayGraph()
print("order after traversing by breadth")
G.bfs('A')
visited={}
print("\n Order after traversing by depth")
G.dfs('A',visited)
