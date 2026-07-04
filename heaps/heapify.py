
#to convert an array into an heap in o(n) instead of o(nlogn) idk thanks to abdul bari
#max heapify and change the signs correspondingly for min
def heapify(arr:list[int]):
    #check from left to right whether each of the element follows the property of the max heap/min heap
    for i in range(len(arr)-1,-1,-1):
        curr=i
        while True:
            largest=curr
            lchild=2*curr+1
            rchild=2*curr+2

            if lchild<len(arr) and arr[lchild]>arr[largest]:
                largest=lchild

            if rchild<len(arr) and arr[rchild]>arr[largest]:
                largest=rchild

            if largest==curr:
                break
            arr[largest],arr[curr]=arr[curr],arr[largest]
            curr=largest
arr=[45, 12, 88, 3, 22, 71, 12, 9, 105, 34, 50, 6, 88, 19]
heapify(arr)
print(arr)