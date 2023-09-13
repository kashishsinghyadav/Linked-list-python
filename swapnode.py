class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        temp=head
        i=1
        while i!=k:
            temp=temp.next
            i+=1
        value=temp.val
        
        temp=head
        prev=None
        
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=temp.next
            temp=nxt
       
        i=1
        temp=prev
        while i!=k:
            temp=temp.next
            i+=1
        value1=temp.val
        temp.val=value
        

        te=prev
       
        temp1=prev

        
        pr=None
        
        while temp1:
            nt=temp1.next
            temp1.next=pr
            pr=temp1
            temp1=temp1.next
            temp1=nt
       

        i=1
        newtp=pr
        h=pr
        while i!=k:
            newtp=newtp.next
            i+=1
       
        newtp.val=value1
        return h

       
       
        
        
       
       


            














