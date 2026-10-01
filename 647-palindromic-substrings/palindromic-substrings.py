class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(n):
            temp = ""

            for j in range(i, n):
                temp += s[j]

                if temp == temp[::-1]:
                    ans += 1

        return ans