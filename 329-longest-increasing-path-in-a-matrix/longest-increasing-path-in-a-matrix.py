class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        path=0
        maxpath=0
        ans=0
        memo = [[0] * n for _ in range(m)]
        def isvalid(row,col):
            if row+1<m and matrix[row+1][col]!=-999 and matrix[row][col] < matrix[row+1][col] :
                return True
            if row-1>=0 and  matrix[row-1][col]!=-999 and matrix[row][col] < matrix[row-1][col] :
                return True
            if col+1<n and  matrix[row][col+1]!=-999 and matrix[row][col] < matrix[row][col+1] :

                return True
            if col-1>=0 and  matrix[row][col-1]!=-999 and matrix[row][col] < matrix[row][col-1] :
                return True
            return False
        def cal(matrix,row,col):
            nonlocal path 
            nonlocal maxpath
            nonlocal ans
            nonlocal memo
            
            if memo[row][col] != 0:
                return memo[row][col]

            path += 1
            current = 1

            if not isvalid(row,col):
                memo[row][col] = 1
                path -= 1
                return 1
            
            if memo[row][col] != 0:
                return memo[row][col]
            if row+1<m and matrix[row+1][col]!=-999 and matrix[row][col] < matrix[row+1][col] :
                current=max(current,1+cal(matrix,row+1,col))
            if row-1>=0 and  matrix[row-1][col]!=-999 and matrix[row][col] < matrix[row-1][col] :
                current=max(current,1+cal(matrix,row-1,col))
            if col+1<n and  matrix[row][col+1]!=-999 and matrix[row][col] < matrix[row][col+1] :

                current=max(current,1+cal(matrix,row,col+1))
            if col-1>=0 and  matrix[row][col-1]!=-999 and matrix[row][col] < matrix[row][col-1] :
                current=max(current,1+cal(matrix,row,col-1))
            memo[row][col] = current
            path -= 1

            return current
           
        for i in range(m):
            for j in range(n):
                ans=max(ans,cal(matrix,i,j))
        return ans

