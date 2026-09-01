class Solution:
    def balancedString(self, s: str) -> int:
        low=0
        high=0
        if len(s) %4 !=0:
            return 0
        t=len(s)//4
        count=len(s)
        set2={}
        for i in range(len(s)):
            if s[i] in set2:
                set2[s[i]]+=1
            else:
                set2[s[i]]=1
        if max(set2.values()) <= t:
            return 0
        for high in range(len(s)):
            set2[s[high]]-=1
            p=max(set2.values())
            while p<=t and low<=high:
                
                count=min(count,high-low+1)
                set2[s[low]]+=1
                low+=1
                p=max(set2.values())
               
                
        if count==len(s):
            return 0
        return count
            