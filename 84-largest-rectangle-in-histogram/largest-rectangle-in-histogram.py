class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxarea=0

        for i,h in enumerate(heights):
            start=i
            while st and st[-1][1]>h:
                p,s=st.pop()
                maxarea=max(maxarea,s*(i-p))
                start=p
            st.append((start,h))
        for i,h in st:
            maxarea=max(maxarea,h* (len(heights)-i))
        return maxarea