from math import inf
#dp[u]+mcs(u,v)<dp[v] puh

def bellmanfordedges(matrix: list[list[int]],source: int,edges,distance): #returns the distance array
    distance[source]=0
    for i in range(len(matrix)):
        flag=False
        for edge in edges:
            u=edge[0]
            v=edge[1]
            cost=edge[2]
            if distance[u]!=inf and distance[u]+cost<distance[v]:
                distance[v]=distance[u]+cost
                flag=True
        if flag and i==len(matrix)-1:
            print("Negative cycle exists!!")
            return False
        elif not flag:
            return True
    return True
def bellmanford(matrix,source,distance):
    edges=[]
    for u in range(len(matrix)):
        for v in range(len(matrix)):
            if matrix[u][v]!=inf:
                edges.append((u,v,matrix[u][v]))
    return bellmanfordedges(matrix,source,edges,distance)


nodes=int(input("Enter the no of nodes: "))
matrix=[list(map(lambda x: inf if x=="inf" else int(x),input().split())) for _ in range(nodes)]
distance=[inf for _ in range(nodes)]
source=int(input("Enter the source:"))
bellmanford(matrix,source,distance)
print(distance)

