class Solution {
public:
    vector<int> satisfaction;
    map<pair<int, int>, int> dp;

    int maxprofit(int i, int j) {
        if (i >= satisfaction.size()) {
            return 0;
        }

        pair<int, int> state = {i, j};

        if (dp.find(state) != dp.end()) {
            return dp[state];
        }

        int take = satisfaction[i] * j + maxprofit(i + 1, j + 1);
        int skip = maxprofit(i + 1, j);

        dp[state] = max(take, skip);

        return dp[state];
    }

    int maxSatisfaction(vector<int>& satisfaction) {
        this->satisfaction = satisfaction;

        sort(this->satisfaction.begin(), this->satisfaction.end());

        return maxprofit(0, 1);
    }
};