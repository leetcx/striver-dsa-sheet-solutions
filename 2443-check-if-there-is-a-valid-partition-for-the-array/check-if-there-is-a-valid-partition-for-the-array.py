class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        def valid(substr1):
            if len(substr1) < 2 or len(substr1) > 3:
                return False

            count = 1
            for i in range(1, len(substr1)):
                if substr1[i] == substr1[i-1]:
                    count += 1

            take = count == len(substr1)

            nottake = len(substr1) == 3
            for j in range(1, len(substr1)):
                diff = substr1[j] - substr1[j-1]
                if diff != 1:
                    nottake = False
                    break

            return take or nottake

        def validof(substr2):
            return valid(substr2)
        dp={}
        def check(i, substr1, substr2):
            if i == len(nums):
                return True
            state=(i,tuple(substr1),tuple(substr2))
            if state in dp:
                return dp[state]
            for j in range(i, min(i+3, len(nums))):
                left = nums[i:j+1]

                if valid(left):
                    if check(j+1, [], []):
                        dp[state]= True
                        return True

            dp[state] =False
            return False

        return check(0, [], [])