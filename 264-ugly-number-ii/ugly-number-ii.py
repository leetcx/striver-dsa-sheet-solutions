class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seq = [1]

        i = j = k = 0

        while len(seq) < n:

            x = min(seq[i] * 2, seq[j] * 3, seq[k] * 5)
            seq.append(x)

            if x == seq[i] * 2:
                i += 1

            if x == seq[j] * 3:
                j += 1

            if x == seq[k] * 5:
                k += 1

        return seq[-1]