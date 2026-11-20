class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degree = [[0] for _ in range(n)]

        for u, v in roads:
            degree[u][0] += 1
            degree[v][0] += 1

        for i in range(len(degree)):
            degree[i].append(i)
        degree.sort(key=lambda x: x[0], reverse=True)
        assign = n
        for t in range(len(degree)):
            degree[t].append(assign)
            assign-=1
        set1={}
        for u,v,w in degree:
            degreeof=u
            index=v
            importance=w
            set1[index]=importance
        maximp=0
        for u,v in roads:
            maximp+=set1[u]+set1[v]
        return maximp

        
        
        

        