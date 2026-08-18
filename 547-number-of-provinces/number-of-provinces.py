class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        n=len(nums)
        province=0
        def dfs(nums,i,j,n):
            
            nums[i][j]=-99
            for k in range(n):
                if nums[j][k] == 1:
                    dfs(nums, j, k, n)
               
        
        for i in range(n):
            for j in range(n):
                if nums[i][j]==1:
                    
                    dfs(nums,i,j,n)
                    
                    province+=1
        return province




