#Creating class graph and performing dfs and bfs
class Graph:
    def __init__(self, directed=False):
        self.graph = {}  
        self.directed = directed 

    def addVertex(self, vertex):
    
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, src, dest):
        
        self.addVertex(src)
        self.addVertex(dest)

        
        self.graph[src].append(dest)

        
        if not self.directed:
            self.graph[dest].append(src)

    def displayGraph(self):
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
            


    
G = Graph(directed=False)  
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
