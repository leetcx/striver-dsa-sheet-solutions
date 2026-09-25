class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        temp = []

        def solve(i):
            if i == len(digits):
                ans.append("".join(temp))
                return

            for ch1 in phone[digits[i]]:
                temp.append(ch1)
                if i+1<len(digits):
                    for ch2 in phone[digits[i+1]]:
                        temp.append(ch2)
                        solve(i+2)
                        temp.pop()
                else:
                    solve(i+1)
                temp.pop()
        solve(0)
        return ans
                