# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr=head
        l=1
        while curr.next:
            curr=curr.next
            l+=1

        curr.next=head

        new_l=l-(k%l)
        while new_l>0:
            curr=curr.next
            new_l-=1

        newhead=curr.next
        curr.next=None
        return newhead
    
