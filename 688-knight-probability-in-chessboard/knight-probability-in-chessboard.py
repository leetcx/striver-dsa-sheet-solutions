class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp={}
        def count(i,j,k):
            if i>=n or i<0 or j<0 or j>=n:
                return 0
            if k==0:
                return 1
            state=(i,j,k)
            if state in dp:
                return dp[state]
            move1=count(i+2, j+1,k-1)



            move2=count(i+2, j-1,k-1)



            move3=count(i-2, j+1,k-1)



            move4=count(i-2, j-1,k-1)



            move5=count(i+1, j+2,k-1)



            move6=count(i+1, j-2,k-1)



            move7=count(i-1, j+2,k-1)



            move8=count(i-1, j-2,k-1)
            dp[state]= (move1+move2+move3+move4+move5+move6+move7+move8)/8
            return dp[state]
        return count(row,column,k)
        
