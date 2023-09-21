class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()
        Rows, Cols = len(grid), len(grid[0])
        
        #bfs traversal of nodes in graph till we are finding "1"
        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0,-1]]  # four possible directions to travel in 2d-matrix
                for dr, dc in directions:
                    ro = dr+row    #final row to travel
                    co = dc+col    #final column to travel
                    #if every condition meets then add travel that node by adding it in queue and visited set
                    if ro in range(Rows) and co in range(Cols) and grid[ro][co] == "1" and not (ro, co) in visited:
                        visited.add((ro,co))
                        queue.append((ro,co))
        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and not (r,c) in visited:
                    #travel in bfs till you are finding "1" in grid and increase islands count after returning back
                    bfs(r,c)
                    islands +=1
        return islands