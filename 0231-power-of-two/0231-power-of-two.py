class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def ipot(n):
            if n == 1:
                return True
            if n==0 or n % 2 != 0:   #to check if odd number 
                return False
            return ipot(n // 2)
        
        return ipot(n)
        