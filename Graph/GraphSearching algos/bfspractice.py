class Queue:
    def __init__(self):
        self.queue=[]

    def isempty(self):
        if len(self.queue)==0:
            return True
        return False

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty!!!")
            return
        data=self.queue[0]
        self.queue=self.queue[1:]
        return data
#adjacency matrix
def breadthfirstsearch(graph,source):
    n=len(graph)
    visited=[False for _ in range(n)]
    queue=Queue()
    parent={source:None}
    visited[source]=True
    queue.enqueue(source)
    while not queue.isempty():
        node=queue.dequeue()
        print(node,end=" ")
        for neighbour in range(n):
            if graph[node][neighbour]==1 and not visited[neighbour]:
                visited[neighbour]=True
                queue.enqueue(neighbour)
                parent[neighbour]=node
    print("\n",parent)
def bfslevel(graph,source):
    parent=[-1 for _ in range(len(graph))]
    level=[-1 for _ in range(len(graph))]
    queue=Queue()
    level[source]=0
    queue.enqueue(source)
    while not queue.isempty():
        node=queue.dequeue()
        for neighbour in range(len(graph)):
            if graph[node][neighbour]==1:
                if level[neighbour]==-1:
                    level[neighbour]=level[node]+1
                    parent[neighbour]=node
                    queue.enqueue(neighbour)
    print(parent,level)
    dest=int(input("Enter the destination:"))
    path=[]
    node=dest
    path.append(node)
    while parent[node]!=-1:
        node=parent[node]
        path.append(node)
    print(path[::-1])
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
source=int(input("Source Node"))
breadthfirstsearch(graph,source)
bfslevel(graph,source)






