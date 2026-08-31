def partition(arr,start,end):
    i=start;pivot=arr[end]
    for j in range(start,end):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1

    arr[i],arr[end]=arr[end],arr[i]
    return i
def quicksort(arr,start,end):
    if start>=end:
        return
    pivot = partition(arr,start,end)
    quicksort(arr,start,pivot-1)
    quicksort(arr,pivot+1,end)
arr = list(map(int,input().split()))
quicksort(arr,0,len(arr)-1)
print(*arr)
