class Solution:
    def longestPalindrome(self, s: str) -> str:
        #fxn to expand outward from centre and check for palindrome
        def expand(l,r):
            while (l>= 0 and r< len(s) and s[l] == s[r]):
                 l-= 1
                 r+=1
            #return string between the pointers till now
            return s[l+1: r]

        result = ""
        for i in range(len(s)):
            #for odd len string
            sub1 = expand(i, i)
            if len(sub1)>len(result):
                result = sub1
            #for even len string
            sub2 = expand(i, i+1)
            if len(sub2)>len(result):
                result = sub2
        return result

        