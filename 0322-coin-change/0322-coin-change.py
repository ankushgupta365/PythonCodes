class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0 #base case
        #for every amount check with all coins if it can be included and calculate minimum coins  to have that amount in dp array
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount] != amount+1 else -1