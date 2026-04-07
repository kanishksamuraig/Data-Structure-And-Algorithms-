def selectionSort(arr):
    for i in range(len(arr)-1):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
arr=[5,4,3,2,1]
selectionSort(arr)
print(arr)
