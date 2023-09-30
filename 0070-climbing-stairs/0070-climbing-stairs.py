class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up Dp solution (true dp solution)
        one = 1  #since steps possible from last end stair
        two = 1  #since steps possible from second last end stari

        #O(n) time and O(1) space
        # since every step can lead to max two step i) +1 and ii) +2 steps so just travers from bottom to up and return last one to reach
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        