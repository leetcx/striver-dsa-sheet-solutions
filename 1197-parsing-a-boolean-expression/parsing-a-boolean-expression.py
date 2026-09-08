class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        operator=s[0]
        current=[]
        st=[]
        if s == 't':
            return True
        if s == 'f':
            return False
        for i in range(1,len(s)):
            if s[i] in ['&','|','!']:
                
                st.append((operator,current))
                operator=s[i]
                current=[]
                continue
            if s[i] == ')':
                
                if operator=='&':
                    result = all(current)
                elif operator=='!':
                    result=not current[0]

                else:
                    result=any(current)
                if st:
                    op, prev = st.pop()
                    prev.append(result)
                    current = prev
                    operator = op
                else:
                    return result
            else:
                if s[i]=='t':
                    current.append(True)
                    continue
                if s[i]=='f':
                    current.append(False)
                    continue
        
          
            
            
        