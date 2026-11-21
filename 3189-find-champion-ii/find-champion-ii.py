class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0] *n
        for u,v in edges:
            indegree[v]+=1
        ans=-1
        count=0
        for i in range(len(indegree)):
            if indegree[i]==0 and count==0:
                ans=i
                count+=1
            elif indegree[i]==0 and count==1:
                return -1
        return ans