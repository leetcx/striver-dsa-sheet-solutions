class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        new=""
        for i in range(len(s)):

            while st and st[-1] == s[i]:
                st.pop()
                break

            else:
                st.append(s[i])
        return "".join(st)
            
