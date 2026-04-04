class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1

    def push(self,data):
        self.top+=1
        self.stack.append(data)

    def pop(self):
        data=self.stack[self.top]
        self.top-=1
        self.stack.pop()
        return data

    def peek(self):
        return self.stack[self.top]

if __name__=="__main__":
    stack=Stack()
    stack.push(1)
    stack.push(100)
    print(stack.stack)
    stack.push(2)
    stack.push(3)
    stack.push(3)
    stack.push(99)
    print(stack.stack)
    stack.pop()
    stack.pop()
    print(stack.stack)


