class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        time=0
        fresh = 0
        q = collections.deque()
        #counting number of fresh and adding rotten to queue to later run bfs bcz dfs won't give right solution here because with bfs we can increase time only after traversing the possible directions with current rotten oranges
        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))     #tuple

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh>0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if (row in range(Rows) and col in range(Cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh-=1
                        q.append((row, col))
            time+=1
        return time if fresh == 0 else -1

        
        