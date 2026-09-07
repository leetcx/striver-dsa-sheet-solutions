class Solution:
    def simplifyPath(self, path: str) -> str:
        
        parts = path.split("/")
        st=[]
        for i in range(1,len(parts)):
            if parts[i]=='...':
                st.append(parts[i])
                continue
            if st and parts[i]=='..':
                st.pop()
                continue
            if parts[i]=='.':
                continue
            if parts[i]!="" and parts[i] != '..':
                st.append(parts[i])
        if not st:
            return '/'
        new=[]
        
        while st:
            new.append(st[-1])
            new.append('/')
            st.pop()
        new.reverse()
        return "".join(new)
            