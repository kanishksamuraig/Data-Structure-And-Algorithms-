from collections import deque
graph = []
def topologicalsort(indegree,ingraph,n,visited):               #here n is the total no of nodes
    queue = deque()
    lst = []
    for nodes in range(len(indegree)):
        if indegree[nodes] == 0 and ingraph[nodes]:
            queue.append(nodes)
    while queue:
        x = queue.popleft()
        ingraph[x] = False
        lst.append(x)
        for neighbours in graph[x]:
            indegree[neighbours]-=1
            if indegree[neighbours]==0:
                queue.append(neighbours)
    return lst


while True:
    x = int(input("Enter the choices \n1) Create new graph\n2) Add edge\n3) Topological sort\n4) Exit\nEnter:"))
    match(x):
        case 1:
            node = int(input("Enter the no of nodes:"))
            graph=[[] for _ in range(node)]
            indegree=[0 for _ in range(node)]
            ingraph=[False for _ in range(node)]
        case 2:
            init,dest = list(map(int,input("Enter Edge in (u v) format:").split()))
            graph[init].append(dest)
            indegree[dest] += 1
            ingraph[init]=ingraph[dest]=True
        case 3:
            n=0
            for i in range(len(ingraph)):
                if ingraph[i]:
                    n+=1
            print(topologicalsort(indegree.copy(),ingraph.copy(),n))
        case 4:
            break
        case _:
            print("Enter the correct choice!!")





