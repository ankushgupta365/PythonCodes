class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #partition not possible if, sum of all elements is odd
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        dp = set()
        dp.add(0) #base case
        for n in nums:
            ndp = set()
            for t in dp:
                if t+n == target:  #sum partition is possible if it found
                    return True
                ndp.add(t+n)
                ndp.add(t)  #adding t also bcz not to remove previous elem, bcz we reassigning 
            dp = ndp
        return True if target in dp else False
        