class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
       
        visited = set()
        def dfs(r,c):
            if (r<0 or r==Rows or c<0 or c==Cols or (r,c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        area = 0
        for r in range(Rows):
            for c in range(Cols):
                area = max(dfs(r,c), area)
        return area