class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            #base case: if out of bounce or already in visited or present height is less then the prev height, which means water cannot be transported
            if (r<0 or c<0 or r == Rows or c == Cols or (r,c) in visited or heights[r][c] < prevHeight):
                return 
            visited.add((r,c))
            neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in neighbours:
                dfs(dr+r, dc+c, visited, heights[r][c])
        
        #visiting all the nodes from top and bottom side
        for c in range(Cols):
            dfs(0, c, pac, heights[0][c])
            dfs(Rows-1, c, atl, heights[Rows-1][c])

        #visiting all the nodes from left and right side
        for r in range(Rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Cols-1, atl ,heights[r][Cols-1])
        
        res = []
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        