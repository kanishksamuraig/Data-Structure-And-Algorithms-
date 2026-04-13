from math import inf
class GraphMat:
    def __init__(self,nodes):
        self.nodes=nodes
        self.graph=list([inf for _ in range(nodes)] for _ in range(nodes))
    
    def addEdges(self,edges):
        for edge in edges:
            u=edge[0]
            v=edge[1]
            weight=edge[2]
            self.graph[u][v]=weight
           #graph[v][u]=weight if it is an undirected graph
    
    def addEdge(self,edge):
        self.graph[edge[0]][edge[1]]=edge[2]

    
    def printgraph(self):    
        for rows in self.graph:
            print(*rows)

class GraphList:
    def __init__(self,nodes):
        self.nodes=nodes
        self.graph=list([] for _ in range(nodes))

    def addEdge(self,edge):
        self.graph[edge[0]].append((edge[1],edge[2]))
    
    def addEdges(self,edges):
        for edge in edges:
            self.graph[edge[0]].append((edge[1],edge[2]))
    
    def printgraph(self):
        for index,rows in enumerate(self.graph):
            print(f"{index}:",*rows)



n=int(input("number of nodes in the Graph:"))
graph=GraphList(n)
while True:
    print("Enter one of the following:\n1)Add edge\n2)Add edges\n3)print graph\n4)exit")
    x=int(input("Enter:"))
    match(x):
        case 1:
            edge=tuple(map(int,input("Enter the edge in u v w format:").split()))
            graph.addEdge(edge)
        case 2:
            e=int(input("Enter the no of edges"))
            edges=[]
            for i in range(e):
                edge=tuple(map(int,input("Enter the edge in u v w format:").split()))
                edges.append(edge)
            graph.addEdges(edges)
        case 3:
            graph.printgraph()
        case 4:
            break
        case _:
            print("Enter a valid option:")
