class Solution:
    def minimumTotal(self, tri: list[list[int]]) -> int:
        p=len(tri)
        n = len(tri)
        memo = [[-999999] * n for _ in range(n)]
        def minpath(tri,row,i):
            nonlocal memo
            if row==len(tri)-1:
                if i>=0 and i<len(tri):
                    return tri[row][i]
            if memo[row][i] != -999999:
                return memo[row][i]
            left=minpath(tri,row+1,i)
            if i+1<len(tri):
                right=minpath(tri,row+1,i+1)  
            memo[row][i]=tri[row][i]+min(left,right) 
            return memo[row][i]
        return minpath(tri,0,0)
        
