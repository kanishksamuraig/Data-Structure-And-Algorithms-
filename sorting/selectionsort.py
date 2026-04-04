def selectionSort(arr: int):
    for i in range(len(arr)-1):
        minidx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minidx]:
                minidx=j
        arr[i],arr[minidx]=arr[minidx],arr[i]
def selectionsortrecursive(arr:int,i,j,minidx):
    if i==len(arr)-1:
        return
    elif j==len(arr):
        arr[minidx],arr[i]=arr[i],arr[minidx]
        selectionsortrecursive(arr,i+1,i+2,i+1)
        return
    if arr[minidx]>arr[j]:
        selectionsortrecursive(arr,i,j+1,j)
    else:
        selectionsortrecursive(arr,i,j+1,minidx)


array=list(map(int,input("Enter the array:").split()))
selectionsortrecursive(array,0,1,0)
print(*array)