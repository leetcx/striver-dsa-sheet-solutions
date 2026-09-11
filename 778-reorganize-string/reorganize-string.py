import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxheap=[]
        set1={}
        for i in s:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for element,frequency in set1.items():
            heapq.heappush(maxheap,(-frequency,element))
        res=""
        while maxheap:
            freq,ele=heapq.heappop(maxheap)
            if len(res)==0 or res[-1] != ele:
                res+=ele
                freq+=1
                if freq<0:
                    heapq.heappush(maxheap,(freq,ele))
            else:
                if maxheap:
                    fr,el=heapq.heappop(maxheap)
                    res+=el
                    fr+=1
                    if fr < 0:
                        heapq.heappush(maxheap,(fr,el))
                    heapq.heappush(maxheap,(freq,ele))
                else:
                    return ""
        return res




        