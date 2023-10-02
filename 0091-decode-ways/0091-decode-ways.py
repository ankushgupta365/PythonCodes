class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  #base case
        
        #from reverse order
        for i in range(len(s)-1, -1, -1):
            #cannot be decoded on its own
            if s[i]=="0":
                dp[i]=0
            else:
                #can be decoded on it's own
                dp[i] = dp[i+1]
            #if can be decoded with two digits then check and get the value
            if i+1<len(s) and (s[i]== "1" or s[i] == '2' and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        #result
        return dp[0]

            