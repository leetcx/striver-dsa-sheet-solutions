class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp={}
        def calculate(i,j,maxMove):
            if i>=m or i<0 or j>=n or j<0:
                return 1 
            if maxMove<=0:
                return 0
            state=(i,j,maxMove)
            if state in dp:
                return dp[state]
            
            move1=0
            move2=0
            move3=0
            move4=0
            if maxMove>0:  
                move1+=calculate(i,j-1,maxMove-1)
                move2+=calculate(i+1,j,maxMove-1)
                move3+=calculate(i,j+1,maxMove-1)
                move4+=calculate(i-1,j,maxMove-1)
            dp[state]=move1+move2+move3+move4 % ((10**9)+7)
            return dp[state]
        return calculate(startRow,startColumn,maxMove) % ((10**9)+7)