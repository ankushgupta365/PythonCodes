class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floy'ds alogorithm of slow and fast pointers 
        slow=0
        fast=0
        while True:
            slow = nums[slow]  
            fast = nums[nums[fast]]
            if slow == fast:  #intersection point
                break     
        
        slow2=0    
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow == slow2: # starting of loop, it means two pointer's point to it, so return this bcz it is dubplicate
                return slow