class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        set1={}
        z=len(p)
        if len(p)> len(s):
            return []
        
        for i in p:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        set2={}
        for i in range(z):
            if s[i] in set2:
                set2[s[i]]+=1
            else:
                set2[s[i]]=1
        if set1==set2:
            ans.append(0)
        low=0
        high=z
        while high<len(s):
            set2[s[low]]=set2.get(s[low],0)-1
            if set2[s[low]]==0:
                del set2[s[low]]
            low+=1
            set2[s[high]]=set2.get(s[high],0)+1
            high+=1
            if set1==set2:
                ans.append(low)
        return ans

        

