class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Define 2 pointers
		ptr1 = list1
        ptr2 = list1
        i, j = 0, 0
		
		# Loop for pointer 1 to reach previous node from a
        while i!=a-1:
            ptr1 = ptr1.next
            i += 1 
			
		# Loop for pointer 2 to reach node b
        while j!=b:
            ptr2 = ptr2.next
            j += 1
			
		# Connect list2 to the next of pointer1
        ptr1.next = list2
		
		# Traverse the list2 till end node
        while list2.next!=None:
            list2 = list2.next
		
		# Assign the next of pointer 2 to the next of list2 i.e connect the remaining part of list1 to list2
        list2.next = ptr2.next
		
		# return final list
        return list1
