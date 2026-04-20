#representation: adjacency list, algorithm: bfs
from collections import deque

def bfs(graph,node,components,compid):
    queue=deque()
    queue.append(node)
    components[node] = compid
    while queue:
        node=queue.popleft()
        for neighbours in graph[node]:
            if components[neighbours]==-1:
                components[neighbours]=compid
                queue.append(neighbours)

def connectedComponents(graph,vertices):
    components=[-1]*vertices
    compid=0
    for i in range(vertices):
        if components[i]==-1:
            bfs(graph,i,components,compid)
            compid+=1
    return compid,components






if __name__=="__main__":
    graph=adj = [[1, 2],[0, 2],[0, 1],[4],[3],[]]
    count,components=connectedComponents(graph,len(graph))
    print(count,components)