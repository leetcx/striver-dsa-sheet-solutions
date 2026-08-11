class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=[]
        for i in range(len(matrix)):
            ans.extend(matrix[i])
        ans.sort()
        if (k-1)>(len(ans)-1):
            return -1
        
        return ans[k-1]