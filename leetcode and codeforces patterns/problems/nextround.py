n,k=list(map(int,input().split()))
contestants=list(map(int,input().split()))
count=0
for i in contestants:
    if i>=contestants[k-1] and i>0:
        count+=1
print(count)