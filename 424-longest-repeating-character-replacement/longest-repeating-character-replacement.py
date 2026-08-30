class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        low=0
        high=0
        seto={}
        res=float('-inf')
        for high in range(0,n):
            if s[high] in seto:
                seto[s[high]]+=1
            else:
                seto[s[high]]=1
            lou=high-low+1
            p=max(seto.values())
            diff=lou-p
            while diff>k:
                seto[s[low]]-=1
                if seto[s[low]]==0:
                    del seto[s[low]]
                low+=1
                lou=high-low+1
                p=max(seto.values())
                diff=lou-p
            lou=high-low+1
            res=max(res,lou)
        return res
            