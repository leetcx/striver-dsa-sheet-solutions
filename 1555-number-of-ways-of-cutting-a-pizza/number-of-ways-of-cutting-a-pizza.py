class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m=len(pizza)
        n=len(pizza[0])
        dp={}
        def hasapple(r1,c1,r2,c2):
            for s in range(r1,r2):
                for q in range(c1,c2):
                    if pizza[s][q]=="A":
                        return True
            return False
        
        def count(i,j,cut):
            if cut==k-1:
                if hasapple(i,j,m,n):
                    return 1
                return 0
            state=(i,j,cut)
            if state in dp:
                return dp[state]
            way=0
            for r in range(i+1,m):
                if hasapple(i,j,r,n) :
                    if hasapple(r,j,m,n) :
                        way+=count(r,j,cut+1)
            for v in range(j+1,n):
                if hasapple(i,j,m,v):
                    if hasapple(i,v,m,n):
                        way+=count(i,v,cut+1)
            dp[state]= way
            return dp[state]
        return count(0,0,0) % (10**9 + 7)

              