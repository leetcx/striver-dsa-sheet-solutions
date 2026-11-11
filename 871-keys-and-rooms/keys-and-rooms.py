from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)
        q=deque()
        visited=[False] * n
        for i in rooms[0]:
            q.append(i)
            visited[i]=True
        visited[0]=True
       
        while q:
            node=q.popleft()
            for p in rooms[node]:
               
                if visited[p]==False:
                    visited[p]=True
                    q.append(p)
        if False in visited:
            return False
        return True
            
            
        
        
        
       
