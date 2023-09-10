class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2) #we are not taking sqrt bcz it is not necessary, dist: distance from origin (since origin is 0,0 so eucladian distance formula reduced to just this)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)  #it will heapify according to first variable, dist which is required

        res = []
        #adiing k closest distances from origins
        while k>0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res
        