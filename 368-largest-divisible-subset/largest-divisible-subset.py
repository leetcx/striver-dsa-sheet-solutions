

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        length = [1] * n      # length[i] = size of subset ending at i
        prev = [-1] * n       # previous index in the subset

        last = 0              # index where largest subset ends

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        prev[i] = j

            if length[i] > length[last]:
                last = i

        ans = []

        while last != -1:
            ans.append(nums[last])
            last = prev[last]

        ans.reverse()
        return ans