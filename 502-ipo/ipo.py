import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(capital)
        temp=[]
        for i in range(n):
            temp.append((capital[i],profits[i]))
        temp.sort()
        idx=0
        maxheap=[]
        while k>0:
            
            
            while idx< n and w>= temp[idx][0]:
                heapq.heappush(maxheap,-temp[idx][1])
                idx+=1
            if maxheap:

                t=-heapq.heappop(maxheap)
                w+=t
            else:
                return w
            k-=1
        return w
            
            

                