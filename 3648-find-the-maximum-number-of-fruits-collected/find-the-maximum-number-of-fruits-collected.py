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

        dp=[[0] * (n+1) for _ in range(m+1)]

        dp[0][n-1]=fruits[0][n-1]

        for i in range(1,m-1):
            for j in range(i+1,n):

                if i+j<n-1:
                    continue

                diag=0
                down=0
                diag2=0

                if j-1>=0:
                    diag=dp[i-1][j-1]

                down=dp[i-1][j]

                if j+1<n:
                    diag2=dp[i-1][j+1]

                dp[i][j]=fruits[i][j]+max(diag,down,diag2)

        q=dp[n-2][n-1]

        mp=[[0] * (n+1) for _ in range(m+1)]

        mp[n-1][0]=fruits[n-1][0]

        for j in range(1,n-1):
            for i in range(j+1,m):

                if i+j<n-1:
                    continue

                diag=0
                down=0
                diag2=0

                if i-1>=0:
                    diag=mp[i-1][j-1]

                down=mp[i][j-1]

                if i+1<m:
                    diag2=mp[i+1][j-1]

                mp[i][j]=fruits[i][j]+max(diag,down,diag2)

        p=mp[n-1][n-2]

        return p+q+child1collects