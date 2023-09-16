class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())   #shallow copy
                return 

            subset.append(nums[i])       
            dfs(i+1)        #including ith elem
            subset.pop()
            dfs(i+1)        #not including ith elem
        dfs(0)
        return res