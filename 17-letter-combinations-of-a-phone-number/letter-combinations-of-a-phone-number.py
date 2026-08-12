class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp=[]
        n=len(digits)
        phone = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv", "9": "wxyz"}
        ans=[]

        def backtrack(digits,n,i):
            if i==n:
                ans.append("".join(temp))
                return
            choice=phone[digits[i]]
            for j in range(len(choice)):
                temp.append(choice[j])
                backtrack(digits,n,i+1)
                temp.pop()
        backtrack(digits,n,0)
        return ans
