import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minheap=[]
        n=len(costs)
        if n < 2 * candidates:
            for i in range(n):
                heapq.heappush(minheap, (costs[i], i))
        else:
            for i in range(0,candidates):
                heapq.heappush(minheap,(costs[i],i))
            for j in range(n-candidates,n):
                heapq.heappush(minheap,(costs[j],j))
        
        cost=0
        
        left=candidates
        right=n-candidates-1
        while k>0:
            if minheap :
                t,idx=heapq.heappop(minheap)
                cost+=t
                
                if left<=right:
                   
                    if  idx<left:
                        heapq.heappush(minheap,(costs[left],left))
                        left+=1
                    else:
                        heapq.heappush(minheap,(costs[right],right))
                        right-=1
            k-=1
            

        return cost

