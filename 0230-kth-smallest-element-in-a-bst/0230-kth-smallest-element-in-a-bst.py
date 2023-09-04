# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        count = 0
        while True:
            while cur:
                #till we go to the left most node (since BST preorder gives sorted values)
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            count +=1
            if count == k:
                return node.val
            cur = node.right
        