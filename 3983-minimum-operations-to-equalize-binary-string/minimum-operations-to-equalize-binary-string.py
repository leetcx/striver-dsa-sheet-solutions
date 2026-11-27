from collections import deque
from sortedcontainers import SortedSet

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        startzero = s.count('0')

        if startzero == 0:
            return 0

        evenzeroes = SortedSet()
        oddzeroes = SortedSet()

        for i in range(n + 1):
            if i % 2 == 0:
                evenzeroes.add(i)
            else:
                oddzeroes.add(i)

        if startzero % 2 == 0:
            evenzeroes.remove(startzero)
        else:
            oddzeroes.remove(startzero)

        q = deque()
        q.append(startzero)

        operation = [-1] * (n + 1)
        operation[startzero] = 0

        while q:
            zero = q.popleft()

            p = max(0, k - n + zero)
            d = min(k, zero)

            low = zero + k - 2 * d
            high = zero + k - 2 * p

            if (zero + k) % 2 == 0:
                current = evenzeroes
            else:
                current = oddzeroes

            for newzero in list(current.irange(low, high)):
                operation[newzero] = operation[zero] + 1
                q.append(newzero)
                current.remove(newzero)

            if operation[0] != -1:
                return operation[0]

        return -1