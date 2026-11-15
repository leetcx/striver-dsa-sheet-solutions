class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indeg=[0] *n
        for u,v in edges:
            indeg[v]+=1
        ans=[]
        for i in range(len(indeg)):

            if indeg[i]==0:
                ans.append(i)
        return ans
