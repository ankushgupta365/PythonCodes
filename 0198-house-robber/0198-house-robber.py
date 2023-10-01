class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp O(n) solution
        #eg. [1,2,3,1] for ind- 2 the r1 and r2 will be 1 and 2 respec and after passing from ind-2 the r2 will be max of prev index + r1 or r2 and r1 will be prev r2.
        r1, r2 = 0,0
        for n in nums:
            temp = max(n+r1, r2)
            r1 = r2
            r2 = temp
        return r2
            