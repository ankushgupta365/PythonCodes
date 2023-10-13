class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  #(index, total)
        def solve(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index,total) in dp:
                return dp[(index,total)]
            
            #total no. of ways of finding target if we add and if we subtract
            dp[(index,total)] = solve(index+1, total+nums[index])+ solve(index+1, total-nums[index])
            return dp[(index,total)]
        return solve(0,0)
        