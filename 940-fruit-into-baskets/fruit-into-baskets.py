class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        high=0
        seto={}
        res=float('-inf')
        for high in range(len(fruits)):
            if fruits[high] in seto:
                seto[fruits[high]]+=1
            else:
                seto[fruits[high]]=1
            lou=high-low+1
            while len(seto)>2:
                seto[fruits[low]]=seto.get(fruits[low],0)-1
                if  seto[fruits[low]]==0:
                    del seto[fruits[low]]
                low+=1
                lou=high-low+1
            if len(seto) <= 2:
                lou=high-low+1
                res=max(res,lou)
        if res==float('-inf'):
            return 0
        return res
            
