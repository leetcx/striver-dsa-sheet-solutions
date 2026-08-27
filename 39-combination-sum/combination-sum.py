class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        n=len(candidates)
        def backtrack(i,target):
            if i==n:
                if target==0:
                    ans.append(temp.copy())
                return
            if candidates[i] > target:
                backtrack(i+1,target)
            else:
                temp.append(candidates[i])
                backtrack(i,target-candidates[i])
                temp.pop()
                
                backtrack(i+1,target)
                
        backtrack(0,target)
        return ans