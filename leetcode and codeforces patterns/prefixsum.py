
# Cumulative sum from the start of the array to a given index.

l=[3,4,5,6,7]
for i in range(1,len(l)):
    l[i]=l[i]+l[i-1]
print(*l)