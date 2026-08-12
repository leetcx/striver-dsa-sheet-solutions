class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(char) for char in row] for row in matrix]
        
        m=len(matrix)
        n=len(matrix[0])
        psum = [[0] * n for _ in range(m)] 

        for i in range(n):
            sum=0
            for j in range(m):
                if matrix[j][i]==1:
                    sum=sum+1
                    psum[j][i]=sum
                else:
                    sum=0
        maxarea=0
        for i in range (m):
            st=[]
            for j,h in enumerate(psum[i]):
                start=j
                while st and st[-1][1]>h:
                    index,height=st.pop()
                    maxarea=max(maxarea,(height*(j-index)))
                    start=index
                st.append((start,h))
            for j,h in st:
                maxarea=max(maxarea,h*(len(psum[i])-j))
        return maxarea

