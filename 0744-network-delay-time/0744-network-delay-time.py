class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time complexity = O(E*logV)
        graph = collections.defaultdict(list)
        #constructing adjacency matrix
        for s,d,w in times:
            graph[s].append([d, w])
        
        minH = [(0, k)]  #source from which our bfs solution for djikstra algorithm start, [weight, node]
        res = 0
        visit = set()
        #bfs djikstra algorithm
        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            visit.add(n1)
            res = w1
            for n2, w2 in graph[n1]:  #visiting neighbours
                if n2 not in visit:
                    heapq.heappush(minH, [w1+w2, n2])   #since total weight to reach that node is: w1+w2
        return res if len(visit) == n else -1
        
        