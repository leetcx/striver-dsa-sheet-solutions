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
        for ele,freq in set1.items():
            heapq.heappush(maxheap,(-freq,ele))
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
                    freq1,ele1=heapq.heappop(maxheap)
                    res+=ele1
                    freq1+=1
                    if freq1<0:
                       heapq.heappush(maxheap,(freq1,ele1))
                    heapq.heappush(maxheap,(freq,ele))
        if len(res) != len(s):
            return ""
        return res

