class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #adjacency list of [dist, node]
        adja = {i: [] for i  in range(len(points))}
        #constructing adjacency list
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)    #manhattan distance
                adja[i].append([dist, j])    #eg: {0: [[4,1], [13,2]], 1: [[4,0], [8, 2]]}
                adja[j].append([dist, i])
        
        #prims alogrithm in bfs
        res=0
        visit = set()
        minHp = [[0,0]]   #[distance, node]
        while len(visit)<len(points):
            dist, i = heapq.heappop(minHp)
            if i in visit:
                continue
            visit.add(i)
            res +=dist
            for neiDist, nei in adja[i]:
                if nei not in visit:
                    heapq.heappush(minHp, [neiDist, nei])
        return res

        


        