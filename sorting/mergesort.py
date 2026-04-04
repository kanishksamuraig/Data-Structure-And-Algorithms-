
def mergeSort(nums, length):
    if (length <= 1):
        return
    middle = length // 2;
    left = [];
    right = []
    for i in range(length):
        if i < middle:
            left.append(nums[i])
        else:
            right.append(nums[i])
    mergeSort(left, middle)
    mergeSort(right, length - middle)
    merge(left, right, nums, length)


def merge(left, right, nums, length):
    i = 0;
    l = 0;
    r = 0;
    leftsize = length // 2;
    rightsize = length - leftsize
    while (l < leftsize and r < rightsize):
        if left[l] < right[r]:
            nums[i] = left[l]
            i += 1
            l += 1
        else:
            nums[i] = right[r]
            i += 1
            r += 1
    while (r < rightsize):
        nums[i] = right[r]
        i += 1
        r += 1
    while (l < leftsize):
        nums[i] = left[l]
        i += 1
        l += 1

if __name__=="__main__":
    import random
    lst=list(range(random.randrange(0,50),(random.randrange(70,80))))
    print(lst)