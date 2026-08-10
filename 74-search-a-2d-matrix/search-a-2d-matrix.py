class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        q=n*m-1
        l=0
        while l<=q:
            mid=(l+q)//2
            i=mid//m
            j=mid%m

            if matrix[i][j]>target:
                q=mid-1
            elif matrix[i][j]<target:
                l=mid+1
            else:
                return True
        return False