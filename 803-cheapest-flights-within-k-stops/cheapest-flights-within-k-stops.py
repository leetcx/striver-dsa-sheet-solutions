class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        p=len(flights)
        res=[float(inf)] * n
        res[src]=0
        for i in range(k+1):
            t=res.copy()
            for k in range(p):
                s=flights[k][0]
                d=flights[k][1]
                wt=flights[k][2]
                if t[d] > res[s]+wt:
                    t[d]=res[s]+wt
            res=t
        if res[dst] == float('inf'):
            return -1
        return res[dst]

