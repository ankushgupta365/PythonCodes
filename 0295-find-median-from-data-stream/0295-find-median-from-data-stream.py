class MedianFinder:

    def __init__(self):
      self.small = []   #max heap
      self.large = []   #min heap
        

    def addNum(self, num: int) -> None:
      heapq.heappush(self.small, -1*num)

      #maintaining small and large heap balance
      if self.small and self.large and ( (self.small[0]*-1)> self.large[0]):
        val = heapq.heappop(self.small)
        heapq.heappush(self.large, -1*val)
      
      #uneven size
      if (len(self.small) - len(self.large)) >1:
        val = heapq.heappop(self.small)
        heapq.heappush(self.large, -1*val)

      if (len(self.large)-len(self.small))>1:
        val = heapq.heappop(self.large)
        heapq.heappush(self.small, -1*val)

        

    def findMedian(self) -> float:
      #if even number of elements 
      if len(self.small) == len(self.large):
        return ((self.small[0]*-1)+self.large[0])/2
      elif len(self.small)>len(self.large):
        return -1*self.small[0]
      else:
        return self.large[0]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()