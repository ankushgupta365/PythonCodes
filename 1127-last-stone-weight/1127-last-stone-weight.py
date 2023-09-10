class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -val for val in stones]
        heapq.heapify(stones) #max heap
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #if one is greater then other then push the difference else do nothing bcz stones will be destroyed so nothing need to be pushed in that case
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)  #if heap become zero size, so base case
        return abs(stones[0])
        