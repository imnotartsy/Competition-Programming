int findSubsetSumEqualsK(vector<int> &nums, int k) {
    vector<vector<bool>> dp(nums.size() + 1, vector<bool>(k + 1));

    for (int i = 0; i <= nums.size(); i++) {
        dp[i][0] = true;
    }

    for (int i = 1; i <= nums.size(); i++) {
        for (int j = 1; j <= k; j++) {
            if (j >= nums[i - 1]) {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp[nums.size()][k];
}