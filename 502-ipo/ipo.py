minheap=[]
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits) 
        temp=[]   
        minheap=[]
        for i in range(n):
            temp.append((capital[i],profits[i]))
        temp.sort()
        if w < temp[0][0]:
            return w
        idx=0
        while k:
            
            while idx <n:
                if w >=temp[idx][0]:
                    heapq.heappush(minheap,-temp[idx][1])
                    idx+=1
                else:
                    break
            if minheap:
                t=-heapq.heappop(minheap)  
                w+=t
            else:
                return w
            k-=1
        return w  
