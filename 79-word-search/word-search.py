class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def solve(i,j,idx,board):
            
            if idx==len(word):
                return True
            
            original=board[i][j]
            board[i][j]=-1
            
            if i-1>=0 and board[i-1][j]==word[idx]:
                if solve(i-1,j,idx+1,board):
                    board[i][j]=original
                    return True
            
            if i+1<m and board[i+1][j]==word[idx]:
                if solve(i+1,j,idx+1,board):
                    board[i][j]=original
                    return True
           
            if j+1<n and board[i][j+1]==word[idx]:
                if solve(i,j+1,idx+1,board):
                    board[i][j]=original
                    return True
            
            if j-1 >=0 and board[i][j-1]==word[idx]:
                if solve(i,j-1,idx+1,board):
                    board[i][j]=original
                    return True
            board[i][j]=original
            return False

            
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]:
                    if solve(i,j,1,board):
                        return True
                    
                
        return False
        