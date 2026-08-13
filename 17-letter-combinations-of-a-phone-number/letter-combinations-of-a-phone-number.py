class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp=[]
        n=len(digits)
        phone = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv", "9": "wxyz"}
        ans=[]
        n=len(digits)

        def back(i):
            if i==n:
                ans.append("".join(temp))
                return
            strop=phone[digits[i]]
            for j in range(len(strop)):
                temp.append(strop[j])
                back(i+1)
                temp.pop()
        back(0)
        return ans
