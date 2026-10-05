class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p = len(text1)
        q = len(text2)

        prev = [0] * (q + 1)

        for i in range(1, p + 1):
            curr = [0] * (q + 1)

            for j in range(1, q + 1):

                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]

                else:
                    curr[j] = max(prev[j], curr[j-1])

            prev = curr

        return prev[q]