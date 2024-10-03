class Graph:
    def __init__(self,edge,N):
        self.adjlist=[[] for _ in range(N)]
        self.indegree=[0]*N

        for(src,dest) in edge:
            self.adjlist[src].append(dest)
            self.indegree[dest]=self.indegree[dest]+1


          

def Findtopologicalvalues(graph,path,discovered,N):
        for v in range(N):
            if(graph.indegree[v]==0 and not discovered[v]):
                for i in graph.adjlist[v]:
                    graph.indegree[i]=graph.indegree[i]-1

                path.append(v)
                discovered[v]=True

                Findtopologicalvalues(graph,path,discovered,N)   

                for i in graph.adjlist[v]:
                  graph.indegree[i]=graph.indegree[i]+1

                path.pop()
                discovered[v]=False


        if len(path) == N:
             print(path)

def printTopologicalOrders(graph):
 
   
    N = len(graph.adjlist)
    discovered = [False] * N
    path = []

    Findtopologicalvalues(graph, path, discovered, N)
 

edges = [(3,4), (1, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

N = 5
graph = Graph(edges, N)
printTopologicalOrders(graph)