class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        n = len(s)

        # --------------------------------
        # Count characters
        # --------------------------------
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        # Only characters occurring at least k times
        chars = []

        for i in range(25, -1, -1):
            if freq[i] >= k:
                chars.append(i)

        # Maximum possible length of answer
        maxlen = sum(freq[i] // k for i in range(26))

        # --------------------------------
        # next occurrence table
        # --------------------------------
        nxt = [[n] * 26 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][ord(s[i]) - 97] = i

        # --------------------------------
        # Check whether curr repeated k times
        # is a subsequence
        # --------------------------------
        def valid(curr):

            pos = 0

            for _ in range(k):
                for ch in curr:

                    p = nxt[pos][ch]

                    if p == n:
                        return False

                    pos = p + 1

            return True

        # --------------------------------
        # DFS
        # --------------------------------
        curr = []

        def dfs():

            # Current prefix itself is a valid answer
            # because we only enter DFS with valid prefixes.
            if len(curr) == maxlen:
                return True

            for ch in chars:

                # Don't exceed available copies
                if curr.count(ch) >= freq[ch] // k:
                    continue

                curr.append(ch)

                # IMPORTANT:
                # prune immediately
                if valid(curr):
                    if dfs():
                        return True

                curr.pop()

            return False

        # --------------------------------
        # Try every possible length
        # --------------------------------
        for length in range(maxlen, 0, -1):

            curr.clear()

            def search():

                if len(curr) == length:
                    return True

                for ch in chars:

                    if curr.count(ch) >= freq[ch] // k:
                        continue

                    curr.append(ch)

                    if valid(curr):
                        if search():
                            return True

                    curr.pop()

                return False

            if search():
                return "".join(chr(c + 97) for c in curr)

        return ""