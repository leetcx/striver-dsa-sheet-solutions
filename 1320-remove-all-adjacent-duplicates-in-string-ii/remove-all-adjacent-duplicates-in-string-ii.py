class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for i in range(len(s)):
            if not st:
                st.append((s[i],1))
                continue
            if st[-1][0] != s[i]:
                st.append((s[i],1))
                continue
            if st[-1][1] < k-1:
                st[-1]=(st[-1][0],st[-1][1]+1)
                continue
            else:
                st.pop()
        ans=[]
        while st:
            d=st[-1][0]
            z=st[-1][1]
            an=z * d
            ans.append(an)
            st.pop()
        ans.reverse()
        return "".join(ans)

