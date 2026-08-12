class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp=[]
        ans=[]
       
        def backtrack(i,target):
            if target== 0 :
                ans.append(temp.copy())
                return
            if target < 0 or i == len(candidates):
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue   
                temp.append(candidates[j])
                backtrack(j+1,target-candidates[j])
                temp.pop()
        backtrack(0,target)
        return ans


        