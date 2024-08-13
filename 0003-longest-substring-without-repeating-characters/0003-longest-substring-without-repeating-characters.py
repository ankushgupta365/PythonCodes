class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charset = set()
        for r in range(len(s)):
            #reset left pointer if not unique character currently
            while s[r] in charset:
                charset.remove(s[l])
                l+=1

            #unique character then add
            charset.add(s[r])
            #updating result 
            res = max(res, r-l+1)
            
        return res


        