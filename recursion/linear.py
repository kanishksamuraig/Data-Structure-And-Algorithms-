def linearsearch(array,n,i,target):
    if i==n:
        return -1
    elif array[i]==target:
        return i
    return linearsearch(array,n,i+1,target)
def binarysearch(array,low,high,x):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if array[mid]==x:
        return mid
    elif array[mid]<x:
        return binarysearch(array,mid+1,high,x)
    else:
        return binarysearch(array,low,mid-1,x)
def bubblesort(array,n):
    k=n
    for i in range(n-1):
        flag=False
        for j in range(k-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                flag=True
        if not flag:
            break
        k-=1
    print(array)
def bubblesortrecursive(array,n,k,i,j):
    if i==n-1:
        print(array)
        return
    elif j==k-1:
        bubblesortrecursive(array,n,k-1,i+1,0)
    else:
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
        bubblesortrecursive(array,n,k,i,j+1)



l=[5,4,3,2,1,6,9,3,2]
print(linearsearch(l,len(l),0,5))
print(binarysearch(l,0,len(l)-1,4))
#bubblesort(l,len(l))
bubblesortrecursive(l,len(l),len(l),0,0)
