def binarysearch(array: list[int],x: int):
    low=0;high=len(array)-1
    while(low<=high):
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
def binarysearchrecursive(array: list[int],low,high,target):
    if low>high:
        return -1

    mid = low+(high-low)//2
    if array[mid]==target:
        return mid
    elif array[mid]<target:
        return binarysearchrecursive(array,mid+1,high,target)
    else:
        return binarysearchrecursive(array,low,mid-1,target)


array=list(map(int,input().split()))
x=int(input("Enter the element to be searched:"))
print(binarysearchrecursive(array,0,len(array)-1,x))
