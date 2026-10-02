class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        m=len(fruits)
        n=len(fruits[0])
        child1collects=0
        for i in range(m):
            for j in range(n):
                if i==j:
                    child1collects+=fruits[i][j]
                    fruits[i][j]=0
        dp=[[-1] * (n+1) for _ in range(m+1)]
        def child2(i,j):
            if i>j or  j<0 or i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return fruits[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            diag=child2(i+1,j-1)
            down=child2(i+1,j)
            diag2=child2(i+1,j+1)
            dp[i][j]=fruits[i][j]+max(diag,down,diag2)
            return dp[i][j]
        child2collects=child2(0,n-1)
        mp=[[-1] * (n+1) for _ in range(m+1)]
        def child3(i,j):
            if i<j or i<0 or j<0 or i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return fruits[i][j]
            if mp[i][j] != -1:
                return mp[i][j]
            diag=child3(i-1,j+1)
            down=child3(i,j+1)
            diag2=child3(i+1,j+1)
            mp[i][j]=fruits[i][j]+max(diag,down,diag2)
            return mp[i][j]
        child3collects=child3(n-1,0)
        z=child1collects+child2collects+child3collects
        return z


        

            