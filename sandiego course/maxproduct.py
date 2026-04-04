import random
def maxpairwiseproduct(array):
    result=0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if result< array[i]*array[j]:
                result=array[i]*array[j]
    return result
def maxpairwiseefficient(array):
    max1=-float('inf');max2=-float('inf')
    index=-1
    for i in range(len(array)):
        if array[i]>max1:
            max1=array[i]
            index=i
    for j in range(len(array)):
        if array[j]>max2 and max1>=array[j] and j!=index:
            max2=array[j]
    return max1*max2
def stresstest():
    i=0
    while i<1000:
        n=random.randrange(11,20);l=[]
        for i in range(n):
            l.append(random.randrange(1000))
        if maxpairwiseefficient(l)!=maxpairwiseproduct(l):
            print("Test case failed")
            print(l)
            print(f"Expected output:{maxpairwiseproduct(l)}\nYour output:{maxpairwiseefficient(l)}")

            break
        else:
            i+=1


stresstest()