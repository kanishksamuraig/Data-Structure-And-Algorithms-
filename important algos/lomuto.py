arr = list(map(int,input().split(",")))
pivot = arr[len(arr)-1];i=0
for j in range(1,len(arr)):
    if arr[j]<pivot:
        arr[j],arr[i]=arr[i],arr[j]
        i+=1
arr[i],arr[len(arr)-1] = arr[len(arr)-1],arr[i]
print(arr)
