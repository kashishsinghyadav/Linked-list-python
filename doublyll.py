class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class LL:
    def __init__(self):
        self.head=None
        
    def insertbeg(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            
        else:
           
            newnode.next=self.head
            
            
            self.head.prev=newnode
            self.head=newnode
            
    def printnode(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end=" ")
            temp=temp.next
        print(None)
            
            
node1=LL()
node1.insertbeg(50)
node1.insertbeg(40)
node1.insertbeg(30)

node1.insertbeg(20)
node1.insertbeg(10)
node1.printnode()

