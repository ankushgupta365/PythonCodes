# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #for every node check in post order that is balanced or not and return, if at any stage any of the root node is not balanced then due to and and logic all the nodes will be non balanced
        def dfsIsBalanced(root):
            if not root:
                return [True,0]
            left = dfsIsBalanced(root.left)
            right = dfsIsBalanced(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, 1+max(left[1], right[1])]
        return dfsIsBalanced(root)[0]
        