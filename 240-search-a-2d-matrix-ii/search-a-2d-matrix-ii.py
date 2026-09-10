class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix[0])
        low = m - 1
        high = 0
        n = len(matrix)

        while low >= 0 and high < n:
            if target == matrix[high][low]:
                return True

            else:
                if target > matrix[high][low]:
                    high += 1
                else:
                    low -= 1

        return False