class Solution:
    def minWindow(self, s: str, t: str) -> str:
        set1={}
        for i in range(len(t)):
            if t[i] in set1:
                set1[t[i]]+=1
            else:
                set1[t[i]]=1
        low=0
        set2={}
        ans=""
        res=float('inf')
        for high in range(len(s)):
            if s[high] in set2:
                set2[s[high]]+=1
            else:
                set2[s[high]]=1
            while all(set2.get(key, 0) >= value for key, value in set1.items()):
               
                lou=high-low+1
                if lou<res:
                    ans=s[low:high+1]
                    res=lou
                set2[s[low]]=set2.get(s[low],0)-1
                if set2[s[low]]==0:
                    del set2[s[low]]
                low+=1
        return ans
            
