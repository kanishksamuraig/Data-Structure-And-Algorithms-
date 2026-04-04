class adjacencyList:
    def __init__(self,nodes):
        self.graph=[[] for _ in range(nodes)]
        self.nodes=nodes
        self.edges=0
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)            # remove in case of directed graph
        self.edges+=1
    def addEdges(self,edges):
        for edge in edges:
            u=edge[0]
            v=edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.edges+=1
    def display(self):
        for index,rows in enumerate(self.graph):
            print(index,*rows,sep="|")
n=int(input("Enter the number of nodes:"))
graph=adjacencyList(n)
while True:
    bole=bool(int(input("Do you want to add an edge(0 for no, 1 for yes):")))
    if not bole:
        break
    graph.addEdge(*list(map(int,input("Enter vertices in u v format:").split())))
graph.display()

