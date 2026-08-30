class Solution:
    def totalFruit(self, s: List[int]) -> int:
        low=0
        high=0
        n=len(s)
        seto={}
        maxi=float(-inf)
        for high in range(0,n):
            if s[high] in seto:
                seto[s[high]] +=1
            else:
                seto[s[high]]=1
            while len(seto) > 2:
                seto[s[low]]-=1
                if seto[s[low]]==0:
                    del seto[s[low]]
                low+=1
            if len(seto) <=2:
                p=high-low+1
                maxi=max(maxi,p)
        return maxi