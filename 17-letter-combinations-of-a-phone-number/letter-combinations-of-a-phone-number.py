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

            # First nested level
            for ch1 in phone[digits[i]]:
                temp.append(ch1)

                # Second nested level
                if i + 1 < len(digits):
                    for ch2 in phone[digits[i + 1]]:
                        temp.append(ch2)

                        # Backtracking handles everything after these 2
                        if i + 2 < len(digits):
                            solve(i + 2)
                        else:
                            ans.append("".join(temp))

                        temp.pop()
                else:
                    ans.append("".join(temp))

                temp.pop()

        solve(0)
        return ans
        