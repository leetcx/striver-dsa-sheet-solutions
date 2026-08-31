class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        low=0
        high=0
        t=len(p)
        if t>len(s):
            return []
        map1={}
        map2={}
        ans=[]
        for i in range(0,t):
            if p[i] in map1:
                map1[p[i]]+=1
            else:
                map1[p[i]]=1
        for high in range(0,len(s)):
            if s[high] in map2:
                map2[s[high]]+=1
            else:
                map2[s[high]]=1
            
            while high-low+1>t:
                map2[s[low]]=map2.get(s[low],0)-1
                if map2[s[low]]==0:
                    del map2[s[low]]
                low+=1
            if map2==map1:
                ans.append(low)
        return ans



            

