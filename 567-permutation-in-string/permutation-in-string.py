class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1={}
        map2={}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] in map1:
                map1[s1[i]]+=1
            else:
                map1[s1[i]]=1
        high=len(s1)-1
        low=0
        for j in range(low,high+1):
            if s2[j] in map2:
                map2[s2[j]]+=1
            else:
                map2[s2[j]]=1
        
        while high < len(s2):
            if map1==map2:
                return True
            map2[s2[low]] = map2.get(s2[low], 0) - 1
            if map2[s2[low]]==0:
                del map2[s2[low]]
            low+=1
            high+=1
            if high==len(s2):
                break
            map2[s2[high]] = map2.get(s2[high], 0) + 1
        return False


