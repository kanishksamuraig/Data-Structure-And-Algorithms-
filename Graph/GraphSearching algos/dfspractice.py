n=int(input("Enter the No of edges"))
graph=[list(map(int,input().split())) for _ in range(n)]
visited={}
parent={}
source=int(input("Enter the source vertex"))
def dfsinit(graph,source):
    for i in range(len(graph)):
        parent[i]=-1
        visited[i]=False
    dfs(graph,source)

def dfs(graph,node):
    visited[node]=True
    for neighbour in range(len(graph)):
        if graph[node][neighbour]==1 and not visited[neighbour]:
            parent[neighbour]=node
            dfs(graph,neighbour)

def path(destination):
    if not visited[destination]:
        print(f"No path exists between src and {destination}")
        return None
    path1=[]
    path1.append(destination)
    node=destination
    while parent[node]!=-1:
        node=parent[node]
        path1.append(node)
    return path1[::-1]
dfsinit(graph,source)
print("Node\tparent\tvisited")
for i in range(n):
    print(i,parent[i],visited[i])
dest=int(input("Enter the destination node:"))
print(path(dest))
    
"""
n=int(input("Enter the No of edges"))
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n
parent=[-1]*n
source=int(input("Enter the source vertex"))
dfs(graph,visited,parent,source)
print("Node\tparent\tvisited")
for i in range(n):
    print(i,parent[i],visited[i])

dest=int(input("Enter the destination node:"))
print(*path(parent,dest))
"""
    

    
