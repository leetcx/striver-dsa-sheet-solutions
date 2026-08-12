class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
       
        def backtrack(i,target):
            if target==0:
                ans.append(temp.copy())
                return 
            if target<0 or i==len(candidates):
                return
            backtrack(i+1,target)


            temp.append(candidates[i])
            backtrack(i,target-candidates[i])
            temp.pop()
        backtrack(0,target)
        return ans            