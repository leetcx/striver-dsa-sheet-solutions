class Solution:
    def countCompleteSubarrays(self, s: List[int]) -> int:
        set2={}
        k=0
        set1={}
        count=0
        low=0
        for i in range(len(s)):
            if s[i] not in set2:
                k+=1

            
                set2[s[i]]=1
        
        for high in range(len(s)):
            if s[high] in set1:
                set1[s[high]]+=1
            else:
                set1[s[high]]=1
            while len(set1)==k:
                count+=len(s)-high
                set1[s[low]]=set1.get(s[low],0)-1
                if set1[s[low]]==0:
                    del set1[s[low]]
                low+=1
        return count
                   