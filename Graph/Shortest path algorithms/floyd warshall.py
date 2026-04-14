#Ak [i,j]=min(A^(k-1)[i,j],A^(k-1)[i,k]+A^(k-1)[i,j])

from math import inf
def floydwarshall(graph):
    for k in range(len(graph)):
        print(f"Iteration:{k}")
        for i in range(len(graph)):
            if i==k:
                continue
            for j in range(len(graph)):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
        for row in graph:
            print(*row)
        for i in range(len(graph)):
            if graph[i][i]<0:
                return False
    return True
n=int(input("Enter the no of nodes in the graph:"))
graph=[list(map(lambda x: inf if x=="inf" else int(x),input().split())) for _ in range(n)]
neg=not floydwarshall(graph)
if neg:
    print("Graph contains negative cycle!!!")