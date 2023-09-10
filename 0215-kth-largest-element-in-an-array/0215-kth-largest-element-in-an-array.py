class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using max heap
        maxHeap = [-val for val in nums]
        heapq.heapify(maxHeap)
        res = -1
        while k>0:
            res = heapq.heappop(maxHeap)
            k-=1
        return res*-1