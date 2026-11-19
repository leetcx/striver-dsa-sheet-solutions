from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        initial="0000"

        deadends=set(deadends)

        if initial in deadends:
            return -1

        q=deque()
        q.append(initial)
        deadends.add(initial)

        level=0

        while q:
            n=len(q)

            while n>0:
                current=q.popleft()

                if current==target:
                    return level

                for i in range(4):
                    do=int(current[i])

                    z=(do+1)%10
                    new=current[:i]+str(z)+current[i+1:]

                    if new not in deadends:
                        q.append(new)
                        deadends.add(new)

                    z=(do-1)%10
                    new2=current[:i]+str(z)+current[i+1:]

                    if new2 not in deadends:
                        q.append(new2)
                        deadends.add(new2)

                n-=1

            level+=1

        return -1