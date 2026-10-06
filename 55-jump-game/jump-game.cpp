class Solution {
public:
    vector<int> dp;
    vector<int> nums;

    bool check(int i) {

        if (i >= nums.size() - 1)
            return true;

        if (nums[i] == 0)
            return false;

        if (dp[i] != -1)
            return dp[i];

        for (int j = i + 1; j <= i + nums[i] && j < nums.size(); j++) {

            bool take = check(j);

            if (take) {
                dp[i] = 1;
                return true;
            }
        }

        dp[i] = 0;
        return false;
    }

    bool canJump(vector<int>& nums) {
        this->nums = nums;
        dp = vector<int>(nums.size(), -1);

        return check(0);
    }
};