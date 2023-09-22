class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}
        for i, n in enumerate(nums):
            if n in hashSet:
                return True
            hashSet[n] = i
        return False
        