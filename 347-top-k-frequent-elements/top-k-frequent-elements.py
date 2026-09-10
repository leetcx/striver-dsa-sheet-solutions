import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap=[]
        set1={}
        for i in nums:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for element,frequency in set1.items():
            if len(minheap) < k:
                heapq.heappush(minheap,(frequency,element))

            else:
                if frequency > minheap[0][0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,(frequency,element))
                    
        res=[]
        while minheap:
            element = heapq.heappop(minheap)[1]

            res.append(element)
            
        return res
