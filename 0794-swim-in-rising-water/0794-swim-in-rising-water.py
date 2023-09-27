class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0],0,0]] #[time/weight, r, c]
        visit = set((0,0))
        directions = [[1,0], [-1, 0], [0,-1], [0,1]]
        #modified version of djikstra algorithm
        while minH:
            w,r,c = heapq.heappop(minH)
            if r == len(grid)-1 and c == len(grid[0])-1:
                return w
            for dr, dc in directions:
                row, col = dr+r, dc+c
                if (row < 0 or col <0 or row == len(grid) or col == len(grid[0]) or (row,col) in visit):
                    continue
                visit.add((row,col))
                heapq.heappush(minH, [max(grid[row][col], w), row, col])   #since we are only adding max distance
        