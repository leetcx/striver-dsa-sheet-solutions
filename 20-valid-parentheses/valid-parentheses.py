class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        ans=[]

        for i in s:
            if i=='(' or i=='{' or i=='[':
                ans.append(i)   
            else:
                if len(ans)==0:
                    return False
                top=ans.pop()
                if i==')' and top!='(':
                    return False
                if i=='}' and top!='{':
                    return False
                if i==']' and top!='[':
                    return False
        return len(ans)==0
                   