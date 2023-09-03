# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validBST(node, left,right):
            if not node:
                return True
            if not (node.val>left and node.val < right):
                return False
            # left< val < right always; so for left node upper limit will change and right node lower limit will change
            return (validBST(node.left, left, node.val) and validBST(node.right, node.val, right))

        #every node should be greater then left and less then right limits
        return validBST(root, float("-inf"), float("inf"))
