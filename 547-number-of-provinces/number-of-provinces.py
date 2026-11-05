from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        p=len(isConnected)
        adj=[[] for _ in range(p)]
        visited=[False] * (p)
        q=deque()
        for i in range(len(isConnected)):
            for j in range(p):
                if i != j and isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        count=0
        for i in range(len(adj)):
            if visited[i]==False:
                visited[i]=True
                count+=1
                q.append(i)
                while q:
                    node=q.popleft()
                    for neigh in adj[node]:
                        if visited[neigh]==False:
                            visited[neigh]=True

                            q.append(neigh)
                   
        return count
                    
