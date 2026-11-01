class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp={}
        def calculate(i,j):
            if i>=m or j>=n:
                return 0
            if matrix[i][j]==0:
                return 0
            state=(i,j)
            if state in dp:
                return dp[state]
            right=1+calculate(i,j+1)
            down=1+calculate(i+1,j)
            diag=1+calculate(i+1,j+1)
            dp[state]= min(right,down,diag)
            return dp[state]
        result=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    result+=calculate(i,j)
        return result
                