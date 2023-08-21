# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Algo: reversve the second half of linked list by reaching there with slow and fast pointers approach and then finnaly merge them
        slow,fast = head,head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        #if list if odd then slow is at middle element and if list is even then slow if at middle link path of middle elements, so assign longer half to first half in case of even linked list
        second=slow.next
        slow.next=None
        prev=None

        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        #merge both halfs now
        second=prev
        first=head
        while second:
           t1,t2=first.next,second.next
           first.next=second
           second.next=t1
           first=t1
           second=t2
        
