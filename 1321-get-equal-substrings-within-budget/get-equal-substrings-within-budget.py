class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        low=0
        high=0
        seto={}
        cost=0
        res=float('-inf')
        for high in range(len(s)):
            
            cost+=abs(ord(s[high])-ord(t[high]))
            lou=high-low+1
            while cost>maxCost and low<high:
                
                cost -= abs(ord(s[low]) - ord(t[low]))
                low+=1
                lou=high-low+1
            if cost<=maxCost:
                lou=high-low+1
                res=max(res,lou)
        if res==float('-inf'):
            return 0
        return res
