class Solution:
    def maximalRectangle(self, m: List[List[str]]) -> int:
        n=len(m)
        p=len(m[0])
        m=[[int(cell) for cell in row] for row in m]
        
        psum = [[0] * p for _ in range(n)]
        
        for i in range(p):
            s=0
            for j in range(n):
                if m[j][i]==1:
                    s=s+1
                    psum[j][i]=s
                else:
                    s=0
        maxarea=0
        g=len(psum)
       
        for l in range(g):
            st=[]
            for i,h in enumerate(psum[l]):
                start=i

                while st and st[-1][1]>h:
                    index,height=st.pop()
                    maxarea=max(maxarea,height*(i-index))
                    start=index
                st.append((start,h))
            for i,h in st:
                maxarea=max(maxarea,h*((len(psum[l])-i)))
        return maxarea
            



