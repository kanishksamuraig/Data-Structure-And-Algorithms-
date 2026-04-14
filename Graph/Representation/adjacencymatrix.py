class Graphmat:
    def __init__(self,N):
        self.graph=list([0 for _ in range(N)] for _ in range(N))
        self.nodes=N
    def addEdges(self,edges: list[int]):
        for edge in edges:
            u=edge[0]
            v=edge[1]
            self.graph[u][v]=1
            self.graph[v][u]=1
    def addEdge(self,u,v):
        if self.graph[u][v]==1:
            print("Edge already entered!!")
        else:
            self.graph[u][v]=1
            self.graph[v][u]=1
    def display(self):
        for row in self.graph:
            print(*row)
    def neighbours(self,node):
        l=[]
        for i in range(self.nodes):
            if self.graph[node][i]==1:
                l.append(i)
        return l




n=int(input())
graph=Graphmat(n)
while True:
    x=bool(int(input("Enter 1 if you want edge else enter 0:")))
    if x:
        edge=list(map(int,input("Enter the number in u v format:").split()))
        graph.addEdge(*edge)
    else:
        break
graph.display()
print(graph.neighbours(1))