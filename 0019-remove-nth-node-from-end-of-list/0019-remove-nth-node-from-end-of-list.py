# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        first=dummy #we are initializing first at dummy bcz we have to delete nth so need to acces n+1 from last
        second=head
        while n !=0:
            second=second.next
            n-=1
        
        while second:
            first=first.next
            second=second.next
        
        first.next=first.next.next
        #returning dummy.next bcz we don't want to include dummy 
        return dummy.next
        

        