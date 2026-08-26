class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        res=[float(inf)] * (n)
        res[src]=0
        
        for i in range(k+1):
            temp=res.copy()
            for j in range(len(flights)):
                s=flights[j][0]
                d=flights[j][1]
                wt=flights[j][2]
                if temp[d] > res[s] + wt:
                    temp[d]= res[s] +wt
            res=temp
        k=res[dst]
        if k == float('inf'):
            return -1
        return k
