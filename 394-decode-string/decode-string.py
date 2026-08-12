class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)
        st=[]
        for i in range(n):
            if s[i]!=']':
                st.append(s[i])
            else:
                k=""
                while st and st[-1]!='[':
                    k=st.pop()+k
                st.pop()
                p=""
                while st and st[-1].isdigit():
                    p=st.pop()+p
                st.append((int(p)*k))
        return "".join(st)
            



