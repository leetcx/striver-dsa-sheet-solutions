class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        temp=[]
        def backtrack(i,sum):
            nonlocal ans
            nonlocal temp
            if sum==target:
                ans.append(temp.copy())
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if sum+candidates[j] <=target:
                    
                    temp.append(candidates[j])
                    backtrack(j+1,sum+candidates[j])
                    temp.pop()
        backtrack(0,0)
        return ans

