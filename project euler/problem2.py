a=2
b=1
c=0
sum=2
while True:#4000000:
    c=a+b
    b=a
    a=c
    if c<=4000000 and c%2==0:
        sum += c
    elif c>4000000:
        break

print(sum)
