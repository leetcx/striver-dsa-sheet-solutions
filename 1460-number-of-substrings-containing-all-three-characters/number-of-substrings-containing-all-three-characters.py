class Solution:
    def numberOfSubstrings(self, s: str) -> int:
       
        set2={}
        low=0
        count=0
        for high in range(len(s)):
            
            if s[high] in set2:
                set2[s[high]]+=1
            else:
                set2[s[high]]=1
            while len(set2)==3:
                count+=len(s)-high
                set2[s[low]]=set2.get(s[low],0)-1
                if set2[s[low]]==0:
                    del set2[s[low]]
                low+=1
        return count


