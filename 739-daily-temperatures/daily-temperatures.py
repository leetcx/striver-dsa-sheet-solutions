class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        res=[0] * len(tem)
        st=[]
        for i in range(len(tem)-1,-1,-1):
            while st and tem[st[-1]] <= tem[i]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            st.append(i)
        return res