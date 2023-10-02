class Solution:
    def countSubstrings(self, s: str) -> int:
        #helper fxn to expand from centre and count palindromic substring
        def expander(l,r):
            res = 0
            #condition for valid palindromic substring, if yes then increase the counter of res
            while (l>=0 and r<len(s) and s[l] == s[r]):
                res += 1
                l-=1
                r+=1
            return res
    
        res=0
        for i in range(len(s)):
            #for odd len strings, call by taking each iteration as center
            res+= expander(i,i)
            #for even len strings, call by taking each iteration as center
            res+= expander(i,i+1)
        return res