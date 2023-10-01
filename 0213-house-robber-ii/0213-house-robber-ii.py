class Solution:
    def rob(self, nums: List[int]) -> int:
        #since every house is connected so we will compute the max rob for subarray's which dont include first element and second element respectively. Also if nums having only one house in it then we will take care of that edge case also.
        return max(nums[0], self.helperofrob(nums[1:]), self.helperofrob(nums[:-1]))

    def helperofrob(self, nums):
        r1, r2 = 0, 0  #dp solution using two variables which store max rob value till lass two houses on each iteration
        for n in nums:
            newRob = max(n+r1, r2)   #(not skipping current, skipping current)
            r1 = r2
            r2 = newRob
        return r2  #since at last we will have maximum of all
        