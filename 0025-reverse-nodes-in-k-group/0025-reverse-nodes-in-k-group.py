# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
             
        dummy = ListNode(0,head)  #dummy node to store initial value for future return
        tail = dummy
        
        while True:
            kth = self.findKth(tail,k)
            if not kth:
                break
            
            gpn = kth.next  #next group node
            curr= tail.next  #current node: starting pt of reverse
            prev = gpn       #end point of reverse: non inclusive
            
            #reverse group
            while curr != gpn:    
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #new head of reversed group and new starting point of next group (non inclusive)
            tmp = tail.next
            tail.next = kth
            tail = tmp
        return dummy.next
    

    def findKth(self,head, k):
        while head and k>0:
            head = head.next
            k-=1
        return head