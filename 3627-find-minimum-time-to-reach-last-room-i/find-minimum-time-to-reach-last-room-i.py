import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(moveTime)
        n=len(moveTime[0])
        minheap=[]
        heapq.heappush(minheap,(0,0,0))
        time=[[float('inf')] *n for _ in range(m)]
        time[0][0]=0
        while minheap:
            timo,row,col=heapq.heappop(minheap)
            if row==m-1 and col==n-1:
                return time[row][col]
            if time[row][col]<timo:
                continue
            for p,k in direction:
                nr=p+row
                nc=k+col
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    if time[row][col]<moveTime[nr][nc]:
                        if time[nr][nc]>moveTime[nr][nc]+1:
                            time[nr][nc]=moveTime[nr][nc]+1
                            heapq.heappush(minheap,(moveTime[nr][nc]+1,nr,nc))
                    else:
                        if time[nr][nc]>time[row][col]+1:
                            time[nr][nc]=time[row][col]+1
                            heapq.heappush(minheap,(time[row][col]+1,nr,nc))
        return -1

