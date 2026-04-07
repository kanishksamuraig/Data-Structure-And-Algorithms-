def insertion(arr):
    for j in range(1,len(arr)):
        i=j
        temp=arr[j]
        while temp<arr[i-1] and i>0:
            arr[i]=arr[i-1]
            i-=1
        arr[i]=temp
l=[10,9,8,1,2,6,4]
insertion(l)
print(l)
