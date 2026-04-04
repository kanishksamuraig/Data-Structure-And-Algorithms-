array=[1,2,3,4,5,6,7,8]
target=7;flag=False
low=0;high=len(array)-1
while(low<=high):
    mid=low+(high-low)//2
    if array[mid]==target:
        print(mid);flag=True
        break
    elif array[mid]<target:
        low=mid+1
    else:
        high=mid-1
print(flag)

