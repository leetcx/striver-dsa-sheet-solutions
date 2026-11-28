
from collections import deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        set1 = {}

        for i in range(n):
            if nums[i] not in set1:
                set1[nums[i]] = []
            set1[nums[i]].append(i)

        maxi = max(nums)
        prime = [True] * (maxi + 1)
        prime[0] = False

        if maxi >= 1:
            prime[1] = False

        for i in range(2, int(maxi ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, maxi + 1, i):
                    prime[j] = False

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        processed = set()
        level = 0

        while q:
            t = len(q)

            while t > 0:
                node = q.popleft()
                t -= 1

                if node == n - 1:
                    return level

                if node - 1 >= 0 and not visited[node - 1]:
                    visited[node - 1] = True
                    q.append(node - 1)

                if node + 1 < n and not visited[node + 1]:
                    visited[node + 1] = True
                    q.append(node + 1)

                z = nums[node]

                if prime[z] and z not in processed:
                    processed.add(z)

                    for keys in range(z, maxi + 1, z):
                        if keys in set1:
                            for p in set1[keys]:
                                if not visited[p]:
                                    visited[p] = True
                                    q.append(p)

            level += 1

        return -1
