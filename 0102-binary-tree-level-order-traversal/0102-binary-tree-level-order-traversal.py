# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = collections.deque()
        if root:
            queue.append(root)
        while queue:
            level = [] #for every level
            for _ in range(len(queue)):
                node = queue.popleft()  
                if node:  #if node not empty add to level and add the left and right node
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level: #if level is not empty then only add it to the res bcz from above line empty nodes can be pushed and level will then not be filled 
                res.append(level)
        return res
        
    
        
        