class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low=0
        high=len(t)-1
        set1={}
        set2={}
        ans=""
        res=float('inf')
        if len(t)>len(s):
            return ""
        for i in range(len(t)):
            if t[i] in set1:
                set1[t[i]]+=1
            else:
                set1[t[i]]=1
        for j in range(0,high+1):
            if s[j] in set2:
                set2[s[j]]+=1
            else:
                set2[s[j]]=1
        while high< len(s) and low<len(s):
            if all(set2.get(key, 0) >= value for key, value in set1.items()):
                l1=high-low+1
                if l1< res:
                    ans=s[low:high+1]
                    res=l1
                
                set2[s[low]]=set2.get(s[low],0)-1
                if set2[s[low]] ==0:
                    del set2[s[low]]
                low+=1
            else:
                high+=1
                if high>=len(s):
                    break
                set2[s[high]]=set2.get(s[high],0)+1
        return ans


