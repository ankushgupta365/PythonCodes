class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Complexity: O(n*m*4^len(word))
        Rows, Cols = len(board), len(board[0])
        visited = set()
        def dfs(r,c,i):
            #if all the words found during dfs
            if i == len(word):
                return True
            #if any of the condition fails return
            if (r<0 or c<0 or r>= Rows or c >=Cols or (r,c) in visited or word[i] != board[r][c]):
                return False
            
            visited.add((r,c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            visited.remove((r,c)) #backtrack
            return res
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r,c, 0):
                    return True
        return False
        