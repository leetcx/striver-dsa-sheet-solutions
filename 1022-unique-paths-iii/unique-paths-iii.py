class Solution:
    def uniquePathsIII(self, board: list[list[int]]) -> int:
        p=len(board)
        z=len(board[0])
        count=0
        temp=[]
        
        for i in range(p):
            for j in range(z):
                if board[i][j]==1:
                    temp.append((i,j))
                    start=i
                    end=j
                if board[i][j]==-1:
                    count+=1
        def solve(i,j,board):
            nonlocal p
            nonlocal z
            nonlocal temp
            
            if i<0 or j<0 or i>=p or j>=z:
                return 0
            if len(temp)>0:
                s,t=temp[-1]
            if board[s][t]==2: 
                if len(temp)==(p*z)-count:
                    return 1
                else:
                    return 0
            
            original=board[i][j]
            board[i][j]=-1
            count1=0
            if i-1>=0 and board[i-1][j] != -1:
                temp.append((i-1,j))
                count1+=solve(i-1,j,board)
                temp.pop()
                
            if j-1>=0 and board[i][j-1] != -1:
                temp.append((i,j-1))
                count1+=solve(i,j-1,board)
                temp.pop()
               
            if i+1<p and board[i+1][j] != -1:
                temp.append((i+1,j))
                count1+=solve(i+1,j,board)
                temp.pop()
                
            if j+1<z and board[i][j+1] != -1:
                temp.append((i,j+1))
                count1+=solve(i,j+1,board)
                temp.pop()
                
            board[i][j]=original
            return count1
        return solve(start,end,board)
            
            
            

            
            
