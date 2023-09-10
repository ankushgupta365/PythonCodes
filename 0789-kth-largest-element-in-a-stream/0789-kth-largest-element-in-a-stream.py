class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #initializing the min heap of size k only
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            #removing extra elements other then k elements in the heap
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)