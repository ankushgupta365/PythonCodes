class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  #base case row
        '''
            start from 2nd last row and move upward from right to left: row[i] = row[i+1]+oldRow[j]
        '''
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
