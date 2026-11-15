class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        parent=[]
        rank=[0] * len(strs)
        for p in range(len(strs)):
            parent.append(p)

        def comparison(st1,st2):
            if len(st1) != len(st2):
                return False
            count=0
            for i in range(len(st1)):
                if st1[i]!=st2[i]:
                    count+=1
            if count>2:
                return False
            return True
        def find(node,parent):
            if node==parent[node]:
                return node
            parent[node]=find(parent[node],parent)
            return parent[node]
        def union(p,q):
            parent_p=find(p,parent)
            parent_q=find(q,parent)
            if parent_p==parent_q:
                return
            if rank[parent_p]>rank[parent_q]:
                parent[parent_q]=parent_p
            elif rank[parent_q]>rank[parent_p]:
                parent[parent_p]=parent_q
            else:
                parent[parent_p]=parent_q
                rank[parent_q]+=1

            
            
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if comparison(strs[i],strs[j]):
                    union(i,j)
        c=0
        for i in range(len(strs)):
            root=find(i,parent)
            if root==i:
                c+=1
        return c
            
                