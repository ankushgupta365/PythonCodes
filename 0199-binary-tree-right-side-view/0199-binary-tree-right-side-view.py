# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])
        while queue:
            rightSide = None #right side node for every level
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node:
                    rightSide = node  #when loops end this will be the rightest node, so add it 
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:  #since we are adding children of null types also into the queue so right side can be of null so check it before addind it to the result
                res.append(rightSide.val)
        return res
                