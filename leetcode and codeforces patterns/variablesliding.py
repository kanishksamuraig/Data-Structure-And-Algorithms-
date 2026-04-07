#longest sequence or substring where< condition>
#longest subarray with sum <= k
arr=[2,5,1,7,10];k=14
left=0;right=0;sum=0
maximum=0
while right<len(arr):
    sum+=arr[right]

    while sum>k:
        sum-=arr[left]
        left+=1

    if sum<=k:
        maximum=max(maximum,right-left+1)
    right+=1
print(maximumi)
