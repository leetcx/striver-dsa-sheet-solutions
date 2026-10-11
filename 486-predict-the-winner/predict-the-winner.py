class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        dp={}
        def calculate(nums, turn):
            if len(nums) == 0:
                return 0
            state=(tuple(nums),turn)
            if state in dp:
                return dp[state]
            pl1 = 0
            pl2 = 0
            pl3 = 0
            pl5 = 0

            if len(nums) > 0 and turn == False:
                pl1 = nums[0] + calculate(nums[1:], True)
                pl2 = nums[-1] + calculate(nums[:-1], True)

            if len(nums) > 0 and turn == True:
                pl5 = calculate(nums[1:], False)
                pl3 = calculate(nums[:-1], False)

            if turn == False:
                dp[state]= max(pl1, pl2)
                return dp[state]
            else:
                dp[state]= min(pl5, pl3)
                return dp[state]

        return calculate(nums, False) >= sum(nums) / 2
