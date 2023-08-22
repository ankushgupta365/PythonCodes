"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy= {None: None}
        cur = head
        while cur:
            copy = Node(cur.val) #creating deep copy
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]   #it will reflect in oldToCopy values next and random
            copy.random = oldToCopy[cur.random]  #we are not doing copy.next = cur.next bcz we want to create deep copy so instead we are referencing from our newly created fresh node from hashmap
            cur = cur.next
        return oldToCopy[head]