class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        low=0
        count=0
        set1={}
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            while len(set1)==3:
                count+=len(s)-high
                
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
        return count
                   