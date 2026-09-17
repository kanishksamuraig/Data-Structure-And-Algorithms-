n = int(input())
sum1=0
for j in range(1,n+1):
    sum2=0;i=1
    while i<j+1:
        if j%i==0:
            sum2+=i
        i+=1
    sum1+=sum2
    sum1 %=(10 ** 9 + 7)
print(sum1%(10**9 + 7))