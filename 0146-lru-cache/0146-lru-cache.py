class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev,self.next = None,None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  #map key to node

        #two dummy ptr to trace Lru and Mru(morst recently used)
        self.left,self.right = Node(0,0),Node(0,0)
        #pointing left and right ptrs to eacher other at starting
        self.left.next=self.right   
        self.right.prev=self.left
        
    #fxn to remove node
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next, nxt.prev = nxt, prev

    #fxn to add node to right
    def insert(self,node):
        nxt,prev=self.right, self.right.prev
        prev.next, nxt.prev = node,node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)