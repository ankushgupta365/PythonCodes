class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #using dp
        dp = [False] * (len(s)+1)
        dp[len(s)] = True   #base case, since "" is found anywhere

        """
            checking from end does, word match with the string and marking dp[i] true if it 
            does, and in future when traverse further left we will store the same value at dp
            [i+len(w)] which will ensure that at that position in the past some word from 
            there has also matched
        """

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]