# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next

        if l<3:
            return [-1,-1]
        else:
            prev=head
            curr=prev.next
            maxi=[]
            mini=[]
            ans=[]
            i=1
            while curr.next:
                i+=1
                if prev.val<curr.val and curr.val>curr.next.val:
                    maxi.append(i)
                elif prev.val>curr.val and curr.val<curr.next.val:
                    mini.append(i)
                prev=prev.next
                curr=curr.next
            ans=maxi+mini
            ans.sort()
            if len(ans)>=2:
                
                v1 = abs(min(j - i for i, j in pairwise(ans)))
                v2=abs(ans[-1]-ans[0])
                if v1>=v2:
                    return [v2,v1]
                else:
                    return [v1,v2]
            else:
                return [-1,-1]
            
        
            
        
                   
