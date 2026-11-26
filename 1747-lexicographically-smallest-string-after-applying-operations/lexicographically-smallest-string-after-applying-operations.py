from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited=set()
        ans=s
        q=deque()
        q.append(s)
        visited.add(s)
        while q:
            node=q.popleft()
            
            ans=min(ans,node)
            new1=list(node)
            for i in range(len(node)):
                if i%2==1:
                    z=int(node[i]) + a
                    if z>9:
                        z=z-10
                    new1[i]=str(z)
            new1 = "".join(new1)

            if new1 not in visited:
                
                q.append(new1)
                visited.add(new1)
            new2=""
            p=len(node)
            new2=node[p-b:]+node[:p-b]
            if new2 not in visited:
                q.append(new2)
                visited.add(new2)
        return ans
                
                    


