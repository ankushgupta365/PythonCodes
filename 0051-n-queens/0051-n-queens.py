class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]  # n*n board with each row: [[".", ".", ".", "."]] if n=4
        col = set() 
        negDiag = set() # (r-c) is unique for every diagnol
        posDiag = set() #(r+c) is unique for every diagnol
        def backtrack(r):
            if r==n:
                ans = ["".join(row) for row in board]   #["..Q."]
                res.append(ans)

            for c in range(n):
                #if this path is not valid place to place queen bcz,at diagnol get killed by others
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                negDiag.add(r-c)
                posDiag.add(r+c)
                col.add(c)
                board[r][c] = "Q"

                backtrack(r+1)
                
                board[r][c]= "."
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                col.remove(c)
        backtrack(0)
        return res



        

        