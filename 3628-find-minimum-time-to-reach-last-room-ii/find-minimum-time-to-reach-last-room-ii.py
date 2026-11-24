import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        m = len(moveTime)
        n = len(moveTime[0])

        time = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]

        minheap = [(0,0,0,0)]
        time[0][0][0] = 0

        while minheap:
            dist, row, col, move = heapq.heappop(minheap)

            if dist > time[row][col][move]:
                continue

            if row == m-1 and col == n-1:
                return dist

            for p,k in direction:
                nr = row+p
                nc = col+k

                if 0 <= nr < m and 0 <= nc < n:

                    wait = max(moveTime[nr][nc] - dist, 0)

                    if move == 0:
                        finaltime = dist + wait + 1
                        nextmove = 1

                    elif move == 1:
                        finaltime = dist + wait + 2
                        nextmove = 0

                    if finaltime < time[nr][nc][nextmove]:
                        time[nr][nc][nextmove] = finaltime
                        heapq.heappush(minheap, (finaltime, nr, nc, nextmove))

        return -1