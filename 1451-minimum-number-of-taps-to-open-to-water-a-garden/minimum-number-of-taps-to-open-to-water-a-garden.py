class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        intervals=[]
        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            intervals.append([left, right]) 
        intervals.sort()
        dp={}
        def cal(i,maxend):
            if i >=len(ranges):
                if maxend>=n:
                    return 0
                return float('inf') 
            state=(i,maxend) 
            if state in dp:
                return dp[state]
            if intervals[i][0] > maxend: 
                dp[state]= float('inf')
                return dp[state]
            open=0
            notopen=0
            
            open = 1 + cal(i + 1, max(maxend, intervals[i][1]))
            notopen=cal(i+1,maxend)
            dp[state]= min(open,notopen)
            return dp[state]
        z=cal(0,0)
        if z==float('inf'):
            return -1
        return z