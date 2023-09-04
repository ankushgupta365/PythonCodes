# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] #global variable
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax,0)
            rightMax = max(rightMax, 0)

            #max value without splitting from that path, possible subtree with max path
            res[0] = max(res[0], root.val+leftMax+rightMax)

            #return max value if this node includes in path
            return root.val + max(leftMax,rightMax)

        dfs(root)
        return res[0]