class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LL:
    def __init__(self):
        self.head=None
        
        
        
        
    def pl(self):
        if self.head is None:
            print('ll is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
        
    def insert(self,data):
        newnode=Node(data)
        
            
        newnode.next=self.head
        self.head=newnode
                

node1=LL()
node1.insert(10)
node1.insert(20)
node1.insert(30)
node1.insert(40)
node1.insert(50)

node1.pl()
