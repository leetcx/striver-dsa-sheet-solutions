class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        seto={}
        res=float('-inf')
        for high in range(0,len(s)):
            if s[high] in seto:
                seto[s[high]]+=1
            else:
                seto[s[high]]=1
            k=high-low+1
            while len(seto) < k:
                seto[s[low]]=seto.get(s[low],0)-1
                if seto[s[low]]==0:
                    del seto[s[low]]
                low+=1
                k=high-low+1
            if len(seto)==k:
                k=high-low+1
                res=max(res,k)
        if res==float('-inf'):
            return 0
        return res
