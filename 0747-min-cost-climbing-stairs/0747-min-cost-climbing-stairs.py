class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp solution O(n)
        cost.append(0) #so that math work out for us
        for i in range(len(cost)-3, -1, -1):   #start from second last element of the original cost arr
            cost[i] = min(cost[i]+cost[i+1], cost[i]+ cost[i+2])  #take min of taking one step or taking two step

        return min(cost[0], cost[1])  #return the minimum cost from either index one or two

        