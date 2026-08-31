try:
    a =10
    b=1
    print(a/b)
except Exception as e:
    print(e)
else:
    print("good you didn't divide using 0")
finally:
    print("Ye i guess you divided it by 0")

    z = ((lambda x,y: x+y)(10,i) for i in range(10))
for i in z:
    print(i)
