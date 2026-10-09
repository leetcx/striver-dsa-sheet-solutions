from functools import lru_cache

class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        m=len(board)
        n=len(board[0])
        dp={}
        @lru_cache(None)
        def find(i,j):
            if i==0 and j==0:
                return (0,1)
            state=(i,j)
            if state in dp:
                return dp[state]
            take1=(float('-inf'),0)
            take2=(float('-inf'),0)
            take3=(float('-inf'),0)
            if i-1>=0 and board[i-1][j] != "X":
                score,ways=find(i-1,j)
                if score != float('-inf'):
                    take1=(score + (int(board[i][j]) if board[i][j].isdigit() else 0),ways)
            if i-1>=0 and j-1>=0 and board[i-1][j-1] != "X":
                score, ways = find(i-1, j-1)
                if score != float('-inf'):
                    take2 = (score + (int(board[i][j]) if board[i][j].isdigit() else 0), ways)

            if j-1>=0 and board[i][j-1] != "X":
                score, ways = find(i, j-1)
                if score != float('-inf'):
                    take3 = (score + (int(board[i][j]) if board[i][j].isdigit() else 0), ways)
            best=max(take1[0],take2[0],take3[0])
            ways=0
            if take1[0]==best:
                ways+=take1[1]
            if take2[0]==best:
                ways+=take2[1]
            if take3[0]==best:
                ways+=take3[1]
            if best == float('-inf'):
                return (float('-inf'),0)
            dp[state]= (best,ways %((10**9)+7))
            return dp[state]
        ans=find(m-1,n-1)
        return [0,0] if ans[0] == float('-inf') else [ans[0],ans[1]]