class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])   #deep copy
                return
            #all subsets that includes nums[i]
            subset.append(nums[i])
            dfs(i+1, subset)

            #all subsets that not includes nums[i] and also any duplicate bcz we are incrementing i
            subset.pop()
            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, subset)

        dfs(0, [])
        return res
