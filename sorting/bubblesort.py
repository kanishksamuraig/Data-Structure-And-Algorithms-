#Bubble sort function
def bubblesort(array: list[int]):
    length=len(array)
    traversal_len=length

    for i in range(length-1): # As 0 to length-1 passes would be required
        traversal_len=length-i
        for j in range(traversal_len-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]


if __name__=="__main__":
    array=list(map(int,input().split()))
    bubblesort(array)
    print(*array)

