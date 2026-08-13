class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        temp=[]
        def backtrack(i,sum1):
            if len(temp)==k and sum1==n:
                ans.append(temp.copy())
                return
            
            for j in range(i,10):
                
                if sum1+j>n:
                    break
                temp.append(j)
                backtrack(j+1,sum1+j)
                temp.pop()
        backtrack(1,0)
        return ans
                

