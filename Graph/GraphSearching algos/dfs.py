#dfs using adjacency list

def dfsinit(graph,parent,visited,source):
    parent=[-1 for i in range(len(graph))]
    visited=[False for i in range(len(graph))]
    dfs(graph,parent,visited,source)
    return (parent,visited)

def dfs(graph,parent,visited,source):
    visited[source]=True
    for neighbour in graph[source]:
        if not visited[neighbour]:
            parent[neighbour]=source
            dfs(graph,parent,visited,neighbour)

def path(parent,destination):
    pathlist = []
    pathlist.append(destination)
    node=destination
    while parent[node] != -1:
        node = parent[node]
        pathlist.append(node)
    return pathlist[::-1]
    
parent,visited=[],[]
n = int(input("Enter the number of nodes in the graph:"))

graph = [list(map(int,input().split())) for _ in range(n)]

print(parent,visited)

source = int(input("Enter the starting vertex:"))

parent,visited = dfsinit(graph,parent,visited,source)

print("Node\tParent\tVisited")

for i in range(n):
    print(f"{i}\t{parent[i]}\t{visited[i]}")
dest=int(input("Enter the destination:"))
print(path(parent,dest))





