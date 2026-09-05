class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count=0
        for top in range(rows):
            temp = [0] * cols

            for bottom in range(top, rows):
                for col in range(cols):
                    temp[col] += matrix[bottom][col]

                set1={0:1}
               
                curr=0
                for i in range(len(temp)):
                    curr+=temp[i]
                    need=curr-target
                    if need in set1:
                        count+=set1[need]
                    set1[curr]=set1.get(curr,0)+1

        return count
