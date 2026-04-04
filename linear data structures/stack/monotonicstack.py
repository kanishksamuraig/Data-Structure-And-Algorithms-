class MonotonicStack:
    def __init__(self,flag):
        self.monotonicstack=[]
        self.isincreasing=flag
        self.top=-1
    def push(self,data):
        if self.isincreasing:
            while self.top>=0 and self.peek()>=data:
                self.pop()
            self.monotonicstack.append(data)
        else:
            while self.top>=0 and self.peek()<=data:
                self.pop()
            self.monotonicstack.append(data)
        self.top += 1
    def pop(self):
        self.monotonicstack.pop()
        self.top-=1

    def peek(self):
        return self.monotonicstack[self.top]

if __name__=="__main__":
    l=[10,20,30,3,2,1];stack=MonotonicStack(False)
    for i in l:
        stack.push(i)
    print(stack.monotonicstack)

