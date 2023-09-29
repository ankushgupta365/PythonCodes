class Solution:
    def findCheapestPrice(self, n: int, grid: List[List[int]], src: int, dst: int, k: int) -> int:
        #constructing adjacency matrix
        adj=[[]for i in range(n)]
        for i in grid:
            adj[i[0]].append([i[1],i[2]])
        dist=[float('inf')for i in range(n)]
        dist[src]=0
        q=[[0,src,0]]
        while q:
            stp,node,cost=q.pop(0)
            if stp>k:
                continue
            for i in adj[node]:
                adjnode,fcost=i[0],i[1]
                if dist[adjnode]>cost+fcost and stp<=k:
                    dist[adjnode]=cost+fcost
                    q.append([stp+1,adjnode,cost+fcost])
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]
