class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        set1={}
        g=""
        for i in t:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        low=0
        res=float('inf')
        set2={}
        for high in range(len(s)):
            if s[high] in set2:
                set2[s[high]]+=1
            else:
                set2[s[high]]=1
            while all(set2.get(k, 0) >= v for k, v in set1.items()) and low<=high:
                if res>high-low+1:
                    res=high-low+1
                    g=s[low:high+1]
                set2[s[low]]=set2.get(s[low],0)-1
                if set2[s[low]]==0:
                    del set2[s[low]]
                low+=1
        return g
