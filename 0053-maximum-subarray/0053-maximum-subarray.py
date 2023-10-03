class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)  #current sum resets to zero if it have become -ve, start forming new subarray
            curSum +=n
            maxSum = max(maxSum, curSum)
        return maxSum

        