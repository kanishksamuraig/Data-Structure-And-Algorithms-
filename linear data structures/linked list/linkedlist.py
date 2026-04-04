#Node definition
class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

#List definition
class LinkedList:
    def __init__(self):
        self.head=None

    #printlist
    def printlist(self):
        if self.head==None:
            print("List is empty")
            return

        curr=self.head
        while(curr.next!=None):
            print(curr.data,end="->")
            curr=curr.next
        print(curr.data)

    #length of the list
    def length(self):
        curr = self.head
        length=0
        while (curr != None):
            length += 1
            curr = curr.next
        return length

    #searches for the element and it will return the index
    def search(self,data):
        curr=self.head
        index=0
        while(curr!=None):
            if curr.data==data:
                return index
            index+=1
            curr=curr.next
        print("Element not found!!")
        return -1

    #inserts the element at the beginning of the list
    def insertatbeginning(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    #inserts at the end of the list
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        curr=self.head
        while(curr.next!=None):
            curr=curr.next
        curr.next=Node(data)

    #inserts element at a specified position
    def insertatpos(self,data,pos):
        length=self.length()
        if pos<1 or pos>length+1:
            print("Invalid position! please Try again!!!")
            return
        elif pos==1:
            self.insertatbeginning(data)
        elif pos==length+1:
            self.insertatend(data)
        else:
            curr=self.head
            for i in range(1,pos-1):
                curr=curr.next
            temp=curr.next
            curr.next=Node(data)
            curr.next.next=temp

    #deletes element at the beginning of the list
    def deleteatbeginning(self):
        if self.head==None:
            print("List is empty!!!")
            return
        self.head=self.head.next

    #deletes at the end of the list
    def deleteatend(self):
        if self.head==None:
            print("List is empty!!!")
            return
        elif self.head.next==None:
            self.head=None
            return
        curr=self.head
        while(curr.next.next!=None):
            curr=curr.next
        curr.next=None

    #deletes the element at the position
    def deleteatpos(self,pos):
        length=self.length()
        if pos<1 or pos>length:
            print("Invalid length!!")
            return
        elif pos==1:
            self.deleteatbeginning()
        elif pos==length:
            self.deleteatend()
        else:
            curr=self.head
            for i in range(1,pos-1):
                curr=curr.next
            temp=curr.next
            curr.next=curr.next.next
            temp.next=None
            del temp

if __name__ =="__main__":
    print("Linked List")
    ll = None
    while(True):
        x=int(input("\nEnter the following\n1)Create a new LinkedList\n2)Insert at the beginning\n3)Insert at the end\n4)Insert at a position\n5)Delete at the beginning\n6)Delete at the end\n7)Delete at a position\n8) print list\n9) Search for an element\n10) Exit\nEnter:"))
        print()
        match(x):
            case 1:
                ll=LinkedList()
            case 2:
                if ll==None:
                    print("list not created!")
                    continue
                data=int(input("Enter the element to be inserted:"))
                ll.insertatbeginning(data)
            case 3:
                if ll == None:
                    print("list not created!")
                    continue
                data = int(input("Enter the element to be inserted:"))
                ll.insertatend(data)

            case 4:
                if ll == None:
                    print("list not created!")
                    continue
                data = int(input("Enter the element to be inserted:"))
                pos=int(input("Enter the position at which the element is to be inserted:"))
                ll.insertatpos(data,pos)

            case 5:
                if ll == None:
                    print("list not created!")
                    continue
                ll.deleteatbeginning()

            case 6:
                if ll==None:
                    print("list not created!")
                    continue
                ll.deleteatend()
            case 7:
                if ll==None:
                    print("list not created!")
                    continue
                pos=int(input("Enter the position where the element is to be deleted:"))
                ll.deleteatpos(pos)
            case 8:
                if ll==None:
                    print("list not created!")
                    continue
                ll.printlist()
            case 9:
                if ll==None:
                    print("list not created!")
                    continue
                element=int(input("Enter the element to find in the list."))
                index=ll.search(element)
                if index!=-1:
                    print(f"element is at position:{index+1}")
            case 10:
                print("Exiting....")
                break
            case _:
                print("Enter the correct value")

