#Messed up the maxheap deletion in such a way that i'm practicing the minheap
class minheap:
    def __init__(self):
        self.heap=[]
        self.size=0

    def insert(self,val):
        self.heap.append(val)
        curr=self.size
        self.size+=1
        while curr>0 and self.heap[curr]<self.heap[(curr-1)//2]:
            temp=self.heap[curr]
            self.heap[curr]=self.heap[(curr-1)//2]
            self.heap[(curr-1)//2]=temp
            curr=(curr-1)//2

    def delete(self):
        val=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.heap.pop()
        curr=0
        self.size-=1
        while True:
            smallest=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<self.size and self.heap[lchild]<self.heap[smallest]:
                smallest=lchild
            if rchild<self.size and self.heap[rchild]< self.heap[smallest]:
                smallest=rchild

            if smallest==curr:
                return val

            self.heap[curr],self.heap[smallest]=self.heap[smallest],self.heap[curr]
            curr=smallest
        return val

    def print(self):
        print(*self.heap)

if __name__=="__main__":
    heap = minheap()
    while True:
        x = int(input("1) Insert\n2) delete\n3) Print\n4) Exit\nEnter"))
        match (x):
            case 1:
                val = int(input("Enter the Value:"))
                heap.insert(val)
            case 2:
                x=heap.delete()
                if x!=-1:
                    print(f"The smallest element currently in the heap is {x}")
            case 3:
                heap.print()
            case 4:
                break
            case '_':
                print("Enter the Correct option")



