class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        totalstones=len(stones)
        compo=0
        visited=[False]*len(stones)
        def dfs(z,i,j):
            visited[z]=True
            for p in range(len(stones)):
                r,c=stones[p]
                if i==r and visited[p]==False:
                    visited[p]=True
                    dfs(p,r,c)
            for t in range(len(stones)):
                r,c=stones[t]
                if c==j and visited[t]==False:
                    visited[t]=True
                    dfs(t,r,c)
            

        for z in range(len(stones)):
            
            if visited[z]==False:
                compo+=1
                dfs(z,stones[z][0],stones[z][1])
        return (totalstones-compo)