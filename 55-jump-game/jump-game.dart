class Solution {
  late List<int> dp;
  late List<int> nums;

  bool check(int i) {
    if (i >= nums.length - 1) {
      return true;
    }

    if (nums[i] == 0) {
      return false;
    }

    if (dp[i] != -1) {
      return dp[i] == 1;
    }

    for (int j = i + 1;
         j <= i + nums[i] && j < nums.length;
         j++) {

      bool take = check(j);

      if (take) {
        dp[i] = 1;
        return true;
      }
    }

    dp[i] = 0;
    return false;
  }

  bool canJump(List<int> nums) {
    this.nums = nums;
    dp = List.filled(nums.length, -1);

    return check(0);
  }
}