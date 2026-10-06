impl Solution {
    fn check(i: usize, nums: &Vec<i32>, dp: &mut Vec<i32>) -> bool {
        if i >= nums.len() - 1 {
            return true;
        }

        if nums[i] == 0 {
            return false;
        }

        if dp[i] != -1 {
            return dp[i] == 1;
        }

        let end = std::cmp::min(nums.len(), i + nums[i] as usize + 1);

        for j in (i + 1)..end {
            let take = Self::check(j, nums, dp);

            if take {
                dp[i] = 1;
                return true;
            }
        }

        dp[i] = 0;
        false
    }

    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut dp = vec![-1; nums.len()];

        Self::check(0, &nums, &mut dp)
    }
}