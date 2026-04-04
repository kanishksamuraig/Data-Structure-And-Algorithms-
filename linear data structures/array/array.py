class Array:
    def __init__(self):
        self.__array=[]
        self.__size=0
    def insertatbegin(self,val:int)->None:
        if self.__size==0:
            self.__array=[val]
            return
        self.__array+=[0]
        for i in range(self.__size,0,-1):
            self.__array[i]=self.__array[i-1]
        self.array[0]=val
    def printarray(self,val:int)->None:
        print(*self.__array)

array=Array()



