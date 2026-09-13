class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for i in range(len(s)):
            if not st:
                st.append((s[i],1))
                continue
            if st and st[-1][0] != s[i]:
                st.append((s[i],1))
                continue
            if st and st[-1][0]==s[i] and st[-1][1] < (k-1):
                st[-1]=(st[-1][0],st[-1][1]+1)
                continue
            st.pop()
        new=[]
        while st:
            p,q=st.pop()
            new.append(p*q)
        new.reverse()
        return "".join(new)


            