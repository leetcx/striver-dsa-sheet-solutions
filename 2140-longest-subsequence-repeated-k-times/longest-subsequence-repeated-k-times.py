class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = []
        temp = []

        p = len(s)
        x = p // k

        set1 = {}

        # Count frequency
        for i in s:
            if i in set1:
                set1[i] += 1
            else:
                set1[i] = 1

        # Find usable characters
        for ch, val in set1.items():
            if val >= k:
                d = ch * (val // k)
                temp.append(d)

        key = "".join(temp)

        # used[0] -> 'a', used[1] -> 'b', ...
        used = [0] * 26

        for m in key:
            used[ord(m) - ord('a')] += 1

        # --------------------------------
        # Build next occurrence table
        # --------------------------------
        n = len(s)

        nxt = [[n] * 26 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][ord(s[i]) - ord('a')] = i

        # --------------------------------
        # Check whether curr repeated k
        # times is a subsequence
        # --------------------------------
        def isvalid(curr):
            pos = 0

            for _ in range(k):
                for ch in curr:

                    p = nxt[pos][ord(ch) - ord('a')]

                    if p == n:
                        return False

                    pos = p + 1

            return True

        new = []

        # --------------------------------
        # Generate candidates
        # --------------------------------
        def found(i):
            nonlocal ans

            if len(new) == i:
                if isvalid("".join(new)):
                    ans = new.copy()
                    return True
                return False

            # Reverse order gives lexicographically largest
            # answer first
            for pot in range(25, -1, -1):

                if used[pot] == 0:
                    continue

                chi = chr(pot + ord('a'))

                new.append(chi)
                used[pot] -= 1

                if found(i):
                    return True

                used[pot] += 1
                new.pop()

            return False

        # Try longest length first
        for i in range(x, -1, -1):
            if found(i):
                return "".join(ans)

        return "".join(ans)