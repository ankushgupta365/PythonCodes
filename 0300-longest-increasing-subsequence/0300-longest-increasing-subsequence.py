class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #classic dp solution: time O(n^2) and space O(n)
        '''
        dp = [1] * len(nums)  #filling dp with base cases
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
        '''
        #binary search solution
        arr = [nums[0]]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n #override
        return len(arr)

        