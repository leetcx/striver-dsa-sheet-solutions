class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        n=len(candidates)
        def backtrack(i,sum):
            if sum==target:
                ans.append(temp.copy())
            for j in range(i,n):
                if sum+candidates[j]<=target:
                    
                    
                    temp.append(candidates[j])
                    backtrack(j,sum+candidates[j])
                    temp.pop()
        backtrack(0,0)
        return ans