def dfs(graph,visited,parent,start):
    visited[start]=True
    for neighbour in range(len(graph)):
        if graph[start][neighbour]==1 and not visited[neighbour]:
            parent[neighbour]=start
            dfs(graph,visited,parent,neighbour)
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
source=int(input("Source Node"))
visited=[False for _ in range(n)]
parent=[-1 for _ in range(n)]
dfs(graph,visited,parent,source)
print(parent)
