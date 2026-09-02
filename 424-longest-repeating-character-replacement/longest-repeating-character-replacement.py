class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        set1={}
        c=len(s)
        res=float('-inf')
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            p = (high - low + 1) - max(set1.values())
            while p>k :
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
                p=(high - low + 1) -max(set1.values())
            res=max(res,high-low+1)
        return res


