
#algo
#perform heapifi on the array
#after performing heapifi perform the deletion operation instead of deallocating the mem location at the end, place that value


#For an ascending order use maxheap and for desc use minheap

def heapifi(arr:list[int]):
    for i in range(len(arr)-1,-1,-1):
        curr=i
        while True:
            large=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<len(arr) and arr[large]<arr[lchild]:
                large=lchild

            if rchild<len(arr) and arr[large]<arr[rchild]:
                large=rchild

            if curr==large:
                break

            arr[large],arr[curr]=arr[curr],arr[large]
            curr=large
def sortbydel(arr):
    size=len(arr)
    while size>0:
        curr=0
        size-=1
        arr[curr],arr[size]=arr[size],arr[curr]
        while True:
            large=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<size and arr[large]<arr[lchild]:
                large=lchild
            if rchild<size and arr[large]<arr[rchild]:
                large=rchild

            if large==curr:
                break

            arr[large],arr[curr]=arr[curr],arr[large]
            curr=large
arr=[45, 12, 88, 3, 22, 71, 12, 9, 105, 34, 50, 6, 88, 19]
heapifi(arr)
sortbydel(arr)
print(arr)