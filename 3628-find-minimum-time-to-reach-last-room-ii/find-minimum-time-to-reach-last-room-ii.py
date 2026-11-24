import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(moveTime)
        n=len(moveTime[0])
        time=[[float('inf')] * n for _ in range(m) ]
        minheap=[]
        heapq.heappush(minheap,(0,0,0))
        time[0][0]=0
        
        while minheap:
            dist,row,col=heapq.heappop(minheap)
            if dist > time[row][col]:
                continue
            if row==m-1 and col==n-1:
                return dist
            
            for p,k in direction:
                nr=p+row
                nc=k+col
                if nr>=0 and nc>=0 and nr<m and nc<n:
                    wait=max(moveTime[nr][nc]-dist,0)
                    finaltime=wait+time[row][col]
                    if (nr+nc)%2==1:
                        if finaltime+1<time[nr][nc]:
                            time[nr][nc]=finaltime+1
                            heapq.heappush(minheap,(finaltime+1,nr,nc))
                           
                    else:
                        if finaltime+2<time[nr][nc]:
                            time[nr][nc]=finaltime+2
                            heapq.heappush(minheap,(finaltime+2,nr,nc))
                            
        return -1
                    