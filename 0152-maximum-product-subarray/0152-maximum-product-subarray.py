class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #kadanes algorithm  O(n) time and O(1) space
        """since nums array can have -ve values which multiplied 
           later can again become positive,so we need to know for 
           future product: min*curr is higher or max*crr is higher. 
           Also we have to take care of zero"""
        maxP = max(nums)  #[0, -1, -4] then -1 will be initial maxP
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmpMax = curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*tmpMax, n*curMin, n)
            maxP = max(maxP, curMax, curMin)
        return maxP
        