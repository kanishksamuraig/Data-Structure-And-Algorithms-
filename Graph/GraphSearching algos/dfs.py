class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.graph = [[0 for _ in range(self.nodes)] for _ in range(self.nodes)]
    def addEdge(self,u,v):
        self.graph[u][v] = 1
        #self.graph[v][u] = 1              # if it is an undirected graph
    def assignGraph(self,graph):
        self.graph = graph
    def dfs(self):
        start = int(input(f"Enter the starting node(0-{self.nodes-1}:"))
        parent=[-1]*self.nodes
        visited = [False]*self.nodes
        self.dfsHelp(start,parent,visited)
        print(parent,visited)
    def dfsHelp(self,node,parent,visited):
        visited[node] = True
        for neighbour in range(self.nodes):
            if self.graph[node][neighbour]==1 and not visited[neighbour]:
                parent[neighbour] = node
                self.dfsHelp(neighbour,parent,visited)
    def connectedComponentsDfs(self):
        visited = [False] * self.nodes
        parent = [-1] * self.nodes
        count=0
        for i in range(self.nodes):
            if not visited[i]:
                self.dfsHelp(i,parent,visited)
                count+=1
        return count
    def detectCycle(self,node,visited,parent=-1):
        visited[node]=True;flag=False
        for neighbour in range(self.nodes):
            if self.graph[node][neighbour]==1  and parent!=neighbour:
                if visited[neighbour]:
                    return True
                flag =flag or self.detectCycle(neighbour,visited,node)
        return flag
nodes = int(input("Enter the number of nodes"))
matrix = [list(map(int,input().split())) for _ in range(nodes)]
graph = Graph(nodes)
graph.assignGraph(matrix)
graph.dfs()
print(f"The no of disconnected components in the graph are {graph.connectedComponentsDfs()}")
visited=[False]*nodes
for i in range(nodes):
    if not visited[i] and graph.detectCycle(i,visited):
        print("Contains cycle")
        break






