from collections import deque
class Graphmat:
    def __init__(self,N : int):
        self.graph=list([0 for _ in range(N)] for _ in range(N))
        self.vertices=N
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
    def bfs(self,start):
        parent={start:None}
        level={start:0}
        queue=deque()
        queue.append(start)
        visited=[False for _ in range(self.vertices)]
        visited[start]=True
        while queue:
            node=queue.popleft()
            for neighbor in range(len(self.graph[node])):
                if self.graph[node][neighbor]==1 and not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append(neighbor)
                    parent[neighbor]=node
                    level[neighbor]=level[node]+1
            print(queue)
        print("Node\tParent\tlevel")
        for i in parent:
            print(i,parent[i],level[i],sep="\t")
    def bfs(self,start,end):
        queue=deque()
        parent={start:None}
        visited=[False for _ in range(self.vertices)]
        level={start:0}
        visited[start]=True
        queue.append(start)
        while queue:
            node=queue.popleft()
            for neighbour in range(len(self.graph[node])):
                if self.graph[node][neighbour]==1 and not visited[neighbour]:
                    queue.append(neighbour)
                    parent[neighbour]=node
                    level[neighbour]=level[node]+1
                    visited[neighbour]=True
        path=[]
        destination=end
        while destination:
            path.append(destination)
            destination=parent[destination]
        print("path:",*path[::-1])



n=int(input())
graph=Graphmat(n)
while True:
    x=bool(int(input("Enter 1 if you want edge else enter 0:")))
    if x:
        edge=list(map(int,input("Enter the number in u v format:").split()))
        graph.addEdge(*edge)
    else:
        break
start=int(input("Enter the starting node:"))
graph.bfs(start)
end=int(input("Enter the destination:"))
graph.bfs(start,end)
