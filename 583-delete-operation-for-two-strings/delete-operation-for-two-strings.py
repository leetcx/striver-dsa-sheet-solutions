class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]* (m+1) for _ in range(n+1)]
        def doit(i,j,word1,word2):
            if i >= n:
                return m-j
            if j>=m:
                return n-i
            if dp[i][j] !=-1:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                return doit(i+1,j+1,word1,word2)
            else:
                a=1+doit(i+1,j,word1,word2)
                b=1+doit(i,j+1,word1,word2)
            dp[i][j]= min (a,b)
            return min(a,b)
        return doit(0,0,word1,word2)
