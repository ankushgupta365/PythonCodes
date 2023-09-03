# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGood(node, maxVal):
            if not node: 
                return 0
            res = 1 if node.val >=maxVal else 0
            maxVal = max(maxVal, node.val)  #for every stack find max for that path till now
            res += findGood(node.left, maxVal)
            res += findGood(node.right, maxVal)
            return res
        return findGood(root, root.val)
        