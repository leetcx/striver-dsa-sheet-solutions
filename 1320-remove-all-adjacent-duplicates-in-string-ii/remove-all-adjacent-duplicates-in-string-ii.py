class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for i in range(len(s)):
            c=s[i]
            if not st:
                st.append((c,1))
                continue
            if st[-1][0] != c:
                st.append((c,1))
                continue
            if st[-1][1] < k-1:
                st[-1] = (st[-1][0], st[-1][1] + 1)
                continue
            st.pop()
        res=[]
        
        while st:
            d=st[-1][0] * st[-1][1]
            res.append(d)
            st.pop()
        res.reverse()
        return "".join(res)         