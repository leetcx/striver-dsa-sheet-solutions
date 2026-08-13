class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        temp = []
        n=len(nums)

        def backtrack():
            if len(temp) == n:
                ans.append(temp.copy())
                return

            seen = set()

            for j in range(len(nums)):
                if nums[j] in seen:
                    continue

                seen.add(nums[j])

                x = nums.pop(j)
                temp.append(x)

                backtrack()

                temp.pop()
                nums.insert(j, x)

        backtrack()
        return ans