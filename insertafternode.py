# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class LL:
#     def __init__(self):
#         self.head=None
        
        
        
        
#     def pl(self):
#         if self.head is None:
#             print('ll is empty')
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data)
#                 temp=temp.next
        
#     def insert(self,data):
#         newnode=Node(data)
        
            
#         newnode.next=self.head
#         self.head=newnode
                

# node1=LL()
# node1.insert(10)
# node1.insert(20)
# node1.insert(30)
# node1.insert(40)
# node1.insert(50)

# node1.pl()
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
    def insertbtw(self,data,val):
        newnode2=Node(data)
        temp=self.head
        while temp.data!=val:
            temp=temp.next

        newnode2.next=temp.next
        temp.next=newnode2

node1=LL()
node1.insert(10)
node1.insert(20)

node1.insert(30)

node1.insert(40)

node1.insert(50)
node1.insertend(10)
node1.insertbtw(60,30)
node1.printll()







