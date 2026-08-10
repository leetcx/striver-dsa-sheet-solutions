class Solution:
    def maximalRectangle(self, m: List[List[str]]) -> int:
        m=[[int(cell) for cell in row] for row in m]
        n=len(m)
        p=len(m[0])
        
        psum = [[0] * p for _ in range(n)]
        for i in range(p):
            sum=0
            for j in range(n):
                if m[j][i]==1:
                    sum+=1
                    psum[j][i]=sum
                else:
                    sum=0
                
        octa=len(psum) ##row
        jio=len(psum[0]) ##column
        
        maxarea=0
        for s in range(octa):
            st=[]
            for i,h in enumerate(psum[s]):
                start=i
                while st and st[-1][1] > h:
                    index,height=st.pop()
                    maxarea= max(maxarea,height *(i-index))
                    start=index
                st.append((start,h))
            for i,h in st:
                maxarea=(max(maxarea,h*(len(psum[s])-i)))
        return maxarea
        
