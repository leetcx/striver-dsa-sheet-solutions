import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        m=len(heights)
        n=len(heights[0])
        res = [[float('inf')] * n for _ in range(m)]
        res[0][0]=0
        pq=[]
        heapq.heappush(pq,(0,(0,0)))
        while pq:
            dist,(row,col)=heapq.heappop(pq)
            if dist> res[row][col]:
                continue
            def valid(k,l,m,n):
                if k>=m or k<0 or l<0 or l>=n:
                    return False
                return True
            for i in range(4):
                r=row+x[i]
                c=col+y[i]
                if not valid(r,c,m,n):
                    continue
                absd=abs(heights[row][col]- heights[r][c])
                wt=max(absd,dist)
                if wt < res[r][c]:
                    res[r][c]=wt
                    heapq.heappush(pq,(wt,(r,c)))
        return res[m-1][n-1]
            
