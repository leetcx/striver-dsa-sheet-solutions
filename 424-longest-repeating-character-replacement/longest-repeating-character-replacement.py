class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        seto={}
        res=float('-inf')
        for high in range(0,len(s)):
            if s[high] in seto:
                seto[s[high]]+=1
            else:
                seto[s[high]]=1
            l1=high-low+1
            diff=l1-max(seto.values())
            while diff>k:
                seto[s[low]]=seto.get(s[low],0)-1
                if seto[s[low]]==0:
                    del seto[s[low]]
                low+=1
                l1=high-low+1
                diff=l1-max(seto.values())
            if diff<=k:
                
                
                res=max(res,l1)
        if res == float('-inf'):
            return 0
        return res
