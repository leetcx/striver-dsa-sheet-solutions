class Solution:
    def nextGreaterElements(self, n: List[int]) -> List[int]:
        n+=n
        l=len(n)
        st=[]
        ans=[0]*l

        for i in range(l-1,-1,-1):
            while st and st[-1]<= n[i]:
                st.pop()
            if len(st)==0:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(n[i])
        return ans[:l//2]