class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1)
            return true;

        vector<int> dp(nums.size(), 0);
        dp[0] = 1;

        for (int i = 0; i < nums.size(); i++) {

            if (dp[i] == 0)
                continue;

            for (int j = i + 1; j < min((int)nums.size(), i + nums[i] + 1); j++) {
                dp[j] = 1;
            }
        }

        return dp[nums.size() - 1] == 1;
    }
};