class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        low=0
        map1={}
        map2={}
        k=len(p)
        high=k-1
        ans=[]
        for i in range(len(p)):
            if p[i] not in map1:
                map1[p[i]]=1
            else:
                map1[p[i]]+=1
        for j in range(low,high+1):
            if s[j] in map2:
                map2[s[j]]+=1
            else:
                map2[s[j]]=1
        while high<len(s) :
            if map1==map2:
                ans.append(low)
            map2[s[low]]=map2.get(s[low],0) -1
            if map2[s[low]] ==0:
                del map2[s[low]]

            low+=1
            high+=1
            if high==len(s):
                break
            map2[s[high]]=map2.get(s[high],0) +1
        return ans


        
