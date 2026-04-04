class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1

    def enqueue(self,data):
        self.queue.append(data)
        self.rear+=1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty!!!")
            return
        data=self.queue[0]
        self.queue=self.queue[1:]
        self.rear-=1
        return data

    def isempty(self):
        if self.rear==-1:
            return True
        return False

    def printqueue(self):
        print(*self.queue)

queue=Queue()
for i in range(5):
    queue.enqueue(i)
queue.printqueue()
print(queue.dequeue())
print(queue.dequeue())
queue.printqueue()
