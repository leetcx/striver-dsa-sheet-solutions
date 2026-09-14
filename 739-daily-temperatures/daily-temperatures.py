class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        res=[0] *len(temp)
        for i in range(len(temp)-1,-1,-1):
            while st and temp[st[-1]] <= temp[i]:
                st.pop()
            
            
            if st:
                res[i]=abs(i-st[-1])
            st.append(i)
        return res
