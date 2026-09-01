class Solution:
    def maxConsecutiveAnswers(self, key: str, k: int) -> int:
        low=0
        high=0
        res=float('-inf')
        set1={}
        for high in range(len(key)):
            if key[high] in set1:
                set1[key[high]]+=1
            else:
                set1[key[high]]=1
            p=max(set1.values())
            while high-low+1-p >k and low<high:
                set1[key[low]]=set1.get(key[low],0)-1
                if set1[key[low]]==0:
                    del set1[key[low]]
                
                low+=1
                p=max(set1.values())
            res=max(res,high-low+1)
        return res