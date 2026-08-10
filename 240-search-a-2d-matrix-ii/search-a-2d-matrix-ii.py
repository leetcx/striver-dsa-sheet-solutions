class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        left=m-1
        right=0

        while left >=0 and right<n:
            if matrix[right][left]==target:
                return True
            if matrix[right][left]>target:
                left-=1
            elif matrix[right][left]<target:
                right+=1
        return False