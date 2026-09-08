class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st=[]
        i=0
        current={}
        n=len(formula)
        while i<len(formula):
            if formula[i]=='(':
                
                st.append(current)
                current={}
                i+=1
            elif formula[i]==')':
                inner=current
                i+=1
                
                multi=""
                while i<len(formula) and formula[i].isdigit():
                    multi+=formula[i]
                    i+=1
                
                if multi == "":
                    multi = "1"
                for k in inner:
                    inner[k]*=int(multi)
                top=st.pop()
               

                for k in inner:
                    top[k] = top.get(k, 0) + inner[k]

                current = top
            else:
                word=""
                if formula[i].isupper():
                    word+=formula[i]
                    i+=1
                    while i<n and formula[i].isalpha() and formula[i].islower():
                        word+=formula[i]
                        i+=1
                    num=""
                    while i<n and formula[i].isdigit():
                        num+=formula[i]
                        i+=1
                    if num == "":
                        num = "1"

                    current[word] = current.get(word, 0) + int(num)
        
        ans = ""

        for atom in sorted(current):
            ans += atom

            if current[atom] > 1:
                ans += str(current[atom])

        return ans

                
                    

                    

                 
                