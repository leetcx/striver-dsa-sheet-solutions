class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res=[float('inf')] * n
        
        res[src]=0
        for i in range(k+1):
            t = res.copy()
            for j in range(len(flights)):
                s=flights[j][0]
                d=flights[j][1]
                wt=flights[j][2]
                if res[s] == float('inf'):
                    continue
                if t[d] > res[s] +wt:
                    t[d]=res[s]+wt
            res=t
        if res[dst] == float('inf'):
            return -1
        return res[dst]
