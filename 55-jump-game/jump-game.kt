class Solution {
    lateinit var dp: IntArray

    fun check(i: Int, nums: IntArray): Boolean {
        if (i >= nums.size - 1) {
            return true
        }

        if (nums[i] == 0) {
            return false
        }

        if (dp[i] != -1) {
            return dp[i] == 1
        }

        val end = minOf(nums.size, i + nums[i] + 1)

        for (j in i + 1 until end) {
            val take = check(j, nums)

            if (take) {
                dp[i] = 1
                return true
            }
        }

        dp[i] = 0
        return false
    }

    fun canJump(nums: IntArray): Boolean {
        dp = IntArray(nums.size) { -1 }
        return check(0, nums)
    }
}