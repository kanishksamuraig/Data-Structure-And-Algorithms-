class DisjointSet:
    def __init__(self,size):
        self.rank = [0] * size
        self.parent = [x for x in range(size)]
    #recursive
    def find(self,value):
        if value!=self.parent[value]:
            return self.find(self.parent[value])
        return value
    #pathcompression
    # def find(self,value):
    #     v = value
    #     if v != self.parent[v]:
    #         v = self.findc(self.parent[value])
    #         self.parent[value] = v
    #     return v
    # #iterative
    # def findi(self,value):
    #     while value!=self.parent[value]:
    #         value = self.parent[value]
    #     return value
    def union(self,u,v):
        ult_parent_u = self.find(u)
        ult_parent_v = self.find(v)
        if ult_parent_u != ult_parent_v:
            if self.rank[ult_parent_u]>=self.rank[ult_parent_v]:
                self.parent[ult_parent_v] = ult_parent_u
                if self.rank[ult_parent_u] == self.rank[ult_parent_v]:
                    self.rank[ult_parent_u] +=1
            else:
                self.parent[ult_parent_u] = ult_parent_v
    def isSameComp(self,u,v):
        return self.find(u)==self.find(v)
    def printrankparent(self):
        print("node\trank\tparent")
        for i in range(len(self.rank)):
            print(f"{i+1}  {self.rank[i]} {self.parent[i]+1}")

#menu driven
dsu = None
while True:
    x = int(input("0) Create a Disjoint set\n1) Find\n2) Union\n3) isSameComp\n4)print\n5)Exit\nEnter:"))
    match(x):
        case 0:
            n = int(input("Enter the number of vertices:"))
            dsu = DisjointSet(n)
        case 1:
            node = int(input("Enter the node you want, to find to which component does it belongs to:"))
            comp = dsu.find(node-1)
            print(comp+1)
        case 2:
            node1,node2 = list(map(int,input("Enter the nodes in ( u v ) format:").split()))
            dsu.union(node1-1,node2-1)
        case 3:
            node1,node2 = list(map(int,input("Enter the nodes in ( u v ) format:").split()))
            if dsu.find(node1-1)==dsu.find(node2-1):
                print("Yes, they belong to the same component")
            else:
                print("No, they don't belong to the same component")
        case 4:
            dsu.printrankparent()
        case 5:
            print("Exiting!!!")
            break
        case _:
            print("Enter the correct option!!!")
=======
    def __init__(self,):
>>>>>>> 372eb918742dcce7ffba48daed3abf12847c54bb
