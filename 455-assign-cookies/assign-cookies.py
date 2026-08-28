class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0
        j=0
        for i in range(len(s)):
            if j>=len(g):
                return res
            if  g[j] <= s[i]:
                res+=1
                
                j+=1
           
        return res


            
