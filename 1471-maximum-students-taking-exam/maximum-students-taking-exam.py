class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m=len(seats)
        n=len(seats[0])
        dp={}
        def maxstu(i,j):
            if i>=m :
                return 0
            state = (i, j, tuple(seats[i - 1]), tuple(seats[i][:j]))
            if state in dp:
                return dp[state]
            take=float('-inf')
            skip=float('-inf')
            if seats[i][j]==".":
               
                if ((j - 1 < 0 or seats[i][j - 1] != "S")and (i - 1 < 0 or j - 1 < 0 or seats[i - 1][j - 1] != "S")and (i - 1 < 0 or j + 1 >= n or seats[i - 1][j + 1] != "S")):
                    seats[i][j]="S"
                    if j + 1 < n:
                        take = 1 + maxstu(i, j + 1)
                        seats[i][j]="."
                        
                    else:
                        take = 1 + maxstu(i + 1, 0)   
                        seats[i][j]="."
            if j + 1 < n:
                skip = maxstu(i, j + 1)
            else:
                skip = maxstu(i + 1, 0)
            dp[state]=max(take,skip)
            return dp[state]
        return maxstu(0,0)
            

                        