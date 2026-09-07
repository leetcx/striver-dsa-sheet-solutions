class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        st.append(s[0])
        for i in range(1,len(s)):
            if s[i]== '*':
                st.pop()
            else:
                st.append(s[i])
        res=[]
        while st:
            res.append(st[-1])
            st.pop()
        res.reverse()
        return "".join(res)
