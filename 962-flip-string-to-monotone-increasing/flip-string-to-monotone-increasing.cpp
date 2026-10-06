class Solution {
public:

    vector<vector<int>> dp;

    int flip(int i, bool choosen1, string &s) {

        if (i >= s.size()) {
            return 0;
        }

        if (dp[i][choosen1] != -1) {
            return dp[i][choosen1];
        }

        int flip1 = INT_MAX;
        int skip1 = INT_MAX;

        if (s[i] == '0' && choosen1 == false) {
            flip1 = 1 + flip(i + 1, true, s);
            skip1 = flip(i + 1, false, s);
        }

        else if (s[i] == '0' && choosen1 == true) {
            flip1 = 1 + flip(i + 1, true, s);
        }

        else if (s[i] == '1' && choosen1 == false) {
            flip1 = 1 + flip(i + 1, false, s);
            skip1 = flip(i + 1, true, s);
        }

        else if (s[i] == '1' && choosen1 == true) {
            skip1 = flip(i + 1, true, s);
        }

        dp[i][choosen1] = min(flip1, skip1);

        return dp[i][choosen1];
    }

    int minFlipsMonoIncr(string s) {

        dp.assign(s.size(), vector<int>(2, -1));

        return flip(0, false, s);
    }
};