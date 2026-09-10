class Solution:
    def kthSmallest(self, matrix: List[List[int]], k1: int) -> int:
        def count(mid):
            row=len(matrix[0])-1
            col=0
            k=0
            while row>=0 and col<len(matrix[0]):
                if  matrix[row][col] > mid:
                    row-=1
                else:
                    k+=row+1
                    col+=1
            return k

        low=matrix[0][0]
        high=matrix[-1][-1]
        res=-1
        while low<=high:
            mid=(low+high)//2
            if count(mid) >=k1:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res