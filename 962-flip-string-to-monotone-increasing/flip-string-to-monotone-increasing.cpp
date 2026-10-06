class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int ones = 0;
        int flip = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') {
                ones++;
            }
            else if (s[i] == '0' && ones > 0) {
                flip = min(flip + 1, ones);
            }
        }

        return flip;
    }
};