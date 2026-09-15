class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1={}
        p=len(s1)
        if p> len(s2):
            return False
        for i in s1:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        set2={}
        for i in range(p):
            if s2[i] in set2:
                set2[s2[i]]+=1
            else:
                set2[s2[i]]=1
        if set1==set2:
            return True
        low=0
        high=p
        while high<len(s2):
            set2[s2[low]]=set2.get(s2[low],0)-1
            if set2[s2[low]]==0:
                del set2[s2[low]]
            low+=1
            set2[s2[high]]=set2.get(s2[high],0)+1
            high+=1
            if set1==set2:
                return True
        return False
            
