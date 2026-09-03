class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        set1={}
        res=float('-inf')
        for high in range(len(fruits)):
            if fruits[high] in set1:
                set1[fruits[high]]+=1
            else:
                set1[fruits[high]]=1
            while len(set1)>2:
                set1[fruits[low]]=set1.get(fruits[low],0)-1
                if set1[fruits[low]]==0:
                    del set1[fruits[low]]
                low+=1
            res=max(res,high-low+1)
        return res
            