class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        d=-1001
        while curr.next:
            if curr.val==curr.next.val:
                d=curr.val

            if curr.val==d:
                prev.next=curr.next




            else:
                prev=prev.next

            curr=curr.next

        if curr.val==d:
            prev.next=None

        return dummy.next
                
