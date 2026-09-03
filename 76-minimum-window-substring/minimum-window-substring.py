class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low=0
        high=0
        set1={}
        have=0
        g=len(t)
        set2={}
        new=""
        res=float('inf')
        for i in range(g):
            if t[i] in set2:
                set2[t[i]]+=1
            else:
                set2[t[i]]=1
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            while all(set1.get(k, 0) >= v for k, v in set2.items()):

                if high-low+1<res:

                    new=s[low:high+1]
                    res=high-low+1
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
        return new
                   