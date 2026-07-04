
class MaxHeap:
    def __init__(self):
        self.heap=[]
        self.size=0
    def insert(self,val:int):
        self.heap.append(val)
        curr=self.size
        self.size+=1

        #check if the parents values are greater than the inserted value else we gonna percolate up
        #perc up
        while curr>0 and self.heap[curr]>self.heap[(curr-1)//2]:
            self.heap[curr],self.heap[(curr-1)//2]=self.heap[(curr-1)//2],self.heap[curr]
            curr=(curr-1)//2

    def delete(self)-> int:
        if self.size==0:
            print("Heap empty!!!")
            return -1

        val = self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heap.pop()
        curr=0
        while True:
            left=2*curr+1
            right=2*curr+2
            largest = curr
            if left <self.size and self.heap[largest]<self.heap[left]:
                largest=left

            if right < self.size and self.heap[largest]<self.heap[right]:
                largest=right

            if largest==curr:
                return val
            self.heap[curr],self.heap[largest]=self.heap[largest],self.heap[curr]
            curr=largest
        # done by me
        #
        # while 2*curr+2 < self.size and (self.heap[curr]< self.heap[2*curr+1] or self.heap[curr]<self.heap[2*curr+2]):
        #     if self.heap[2*curr+2]>=self.heap[2*curr+1]:
        #         self.heap[curr],self.heap[2*curr+2]=self.heap[2*curr+2],self.heap[curr]
        #         curr=2*curr+2
        #     else:
        #         self.heap[curr], self.heap[2 * curr + 1] = self.heap[2 * curr + 1], self.heap[curr]
        #         curr=2*curr+1
        # while 2*curr+1 <self.size and self.heap[curr]<self.heap[2*curr+1]:
        #     self.heap[curr], self.heap[2 * curr + 1] = self.heap[2 * curr + 1], self.heap[curr]
        #     curr = 2 * curr + 1
        return val
    def print(self):
        print(*self.heap)
heap=MaxHeap()
while True:
    x=int(input("1) Insert\n2) delete\n3) Print\n4) Exit\nEnter"))
    match(x):
        case 1:
            val = int(input("Enter the Value:"))
            heap.insert(val)
        case 2:
            print(f"The greatest element currently in the heap is {heap.delete()}")
        case 3:
            heap.print()
        case 4:
            break
        case '_':
            print("Enter the Correct option")
