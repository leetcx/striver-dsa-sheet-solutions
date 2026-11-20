from collections import deque

class Solution:
    def buildMatrix(self, k: int, row: list[list[int]], col: list[list[int]]) -> list[list[int]]:
        indeg1=[0] *k
        indeg2=[0]*k
        adj=[[] for _ in range(k)]
        adj1=[[] for _ in range(k)]

        for u,v in row:
            indeg1[v-1]+=1
            adj[u-1].append(v-1)

        for u,v in col:
            indeg2[v-1]+=1
            adj1[u-1].append(v-1)

        def bfs(indegree,adjacent):
            q=deque()
            ans=[]

            for p in range(len(indegree)):
                if indegree[p]==0:
                    q.append(p)

            while q:
                node=q.popleft()
                ans.append(node)

                for neigh in adjacent[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        q.append(neigh)

            if len(ans) != k:
                return []
            return ans

        rowbfs=bfs(indeg1,adj)
        colbfs=bfs(indeg2,adj1)

        if not rowbfs or not colbfs:
            return []

        set1={}
        set2={}

        for i in range(k):
            set1[rowbfs[i]]=i
            set2[colbfs[i]]=i

        ansmatrix=[[0] *k for _ in range(k)]

        for t in range(k):
            ansmatrix[set1[t]][set2[t]]=t+1

        return ansmatrix