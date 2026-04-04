#recursive
def linearsearchrecursive(i:int,l:list,x:int)->int:
    if i==len(l):
        return -1
    elif x==l[i]:
        return i
    else:
        return linearsearchrecursive(i+1,l,x)
#loop
def linearsearchiterative(l:list[int],x:int)->int:
    for i in range(len(l)):
        if x==l[i]:
            return i
    return -1
l=list(map(int,input("Enter the list with space:").split()))
x=int(input("Enter the number to search:"))
print(linearsearchrecursive(0,l,x))
print(linearsearchiterative(l,x))
