# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next if slow.next else None
            fast = fast.next.next if fast.next.next else None
            if slow == fast:
                return True
        return False