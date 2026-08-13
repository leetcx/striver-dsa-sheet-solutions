class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        ans = []
        temp = []

        def backtrack(i, total):
            if total == target:
                ans.append(temp.copy())
                return

            if i == len(cand) or total > target:
                return

            for j in range(i, len(cand)):

                if j > i and cand[j] == cand[j - 1]:
                    continue

                if total + cand[j] > target:
                    break

                temp.append(cand[j])
                backtrack(j + 1, total + cand[j])
                temp.pop()

        backtrack(0, 0)
        return ans