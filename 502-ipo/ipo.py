import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        temp=[]
        for i in range (len(profits)):
            a=profits[i]
            b=capital[i]
            temp.append((b,a))
        temp.sort()
        idx=0
        maxheap=[]
        while k:
            while idx<len(profits):
                if temp[idx][0]>w:
                    break
                heapq.heappush(maxheap,-temp[idx][1])
                idx+=1
            if maxheap:
                p=heapq.heappop(maxheap)
                w+=-(p)
            else:
                return w
            k-=1
        return w

                