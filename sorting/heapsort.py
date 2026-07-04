
#algo
#perform heapify on the array
#after performing heapify perform the deletion operation instead of deallocating the mem location at the end, place that value


#For an ascending order use maxheap and for desc use minheap

def heapify(arr:list[int]):
    for i in range(len(arr)-1,-1,-1):
        curr=i
        while True:
            largest=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<len(arr) and arr[largest]<arr[lchild]:
                largest=lchild

            if rchild<len(arr) and arr[largest]<arr[rchild]:
                largest=rchild

            if curr==largest:
                break

            arr[largest],arr[curr]=arr[curr],arr[largest]
            curr=largest
def sortbydel(arr):
    size=len(arr)
    while size>0:
        curr=0
        size-=1
        arr[curr],arr[size]=arr[size],arr[curr]
        while True:
            largest=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<size and arr[largest]<arr[lchild]:
                largest=lchild
            if rchild<size and arr[largest]<arr[rchild]:
                largest=rchild

            if largest==curr:
                break

            arr[largest],arr[curr]=arr[curr],arr[largest]
            curr=largest
arr=[45, 12, 88, 3, 22, 71, 12, 9, 105, 34, 50, 6, 88, 19]
heapify(arr)
sortbydel(arr)
print(arr)