def minrotated(nums):
    low=0;
    min=nums[0]
    high=len(nums)-1;
    while low<=high:
        mid=low+(high-low)//2
        if nums[low]<=nums[high]:
            return min
        else:
            if nums[mid]<min:
                min=nums[mid]
            low=mid+1
    return min

nums=[6,7,0,1,2,3,4,5]
print(minrotated(nums))