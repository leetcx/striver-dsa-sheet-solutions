class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        low=0
        set2={}
        high=k-1
        res=float('-inf')
        p=0
        for i in range(low,high+1):
            if s[i] in set2:
                set2[s[i]]+=1
            else:
                set2[s[i]]=1
        while high< len(s):
            p = sum(set2.get(x, 0) for x in "aeiou")
            
            res=max(res,p)
            set2[s[low]]=set2.get(s[low],0)-1
            if set2[s[low]]==0:
                del set2[s[low]]
            low+=1
            high+=1
            if high>=len(s):
                break
            set2[s[high]]=set2.get(s[high],0)+1
        return res



                       
                        
                        
