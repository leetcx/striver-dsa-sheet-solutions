import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap=[]
        set1={}
        for i in tasks:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for elem,frequency in set1.items():
            heapq.heappush(maxheap,(-frequency,elem))
        time=0
        while maxheap:
            temp=[]
            for i in range(n+1):
                if maxheap:
                    fre,ele=heapq.heappop(maxheap)
                    fre+=1
                    if fre < 0:
                        temp.append((fre,ele))
                    time+=1
                elif temp:
                    time+=1

            for i in temp:
                heapq.heappush(maxheap,i)
        return time
                

