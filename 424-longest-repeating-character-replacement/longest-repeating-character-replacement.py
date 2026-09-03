class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        set1={}
        res=float('-inf')
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            p=max(set1.values())
            while (high-low+1)-p>k and low<=high:
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
            res=max(res,high-low+1)
        return res