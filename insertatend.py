class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def printll(self):
        if self.head is None:
            print("ll is mepty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next 

    def insert(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insertend(self,data):
        newnode1=Node(data)
        if not self.head:
            self.head=newnode1
        else:
            temp=self.head
            while temp.next:
                temp=temp.next

            temp.next=newnode1
            newnode1.next=None

node1=LL()
node1.insert(10)
node1.insert(20)

node1.insert(30)

node1.insert(40)

node1.insert(50)
node1.insertend(10)
node1.printll()






