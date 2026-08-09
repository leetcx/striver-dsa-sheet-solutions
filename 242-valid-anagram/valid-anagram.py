class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        set1={}
        g=len(s)
        p=len(t)
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        return freq == set1
           
        