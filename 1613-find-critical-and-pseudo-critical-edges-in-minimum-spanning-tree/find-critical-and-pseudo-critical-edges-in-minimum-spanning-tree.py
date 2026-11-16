
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])

        def kruskal(edges,skip,add):
            rank = [0] * n
            parent = [i for i in range(n)]

            def find(x,parent):
                if parent[x] == x:
                    return x
                parent[x] = find(parent[x],parent)
                return parent[x]

            def union(x, y):
                parent_x = find(x,parent)
                parent_y = find(y,parent)

                if parent_x == parent_y:
                    return 

                if rank[parent_x] > rank[parent_y]:
                    parent[parent_y] = parent_x
                elif rank[parent_x] < rank[parent_y]:
                    parent[parent_x] = parent_y
                else:
                    parent[parent_x] = parent_y
                    rank[parent_y] += 1

               

            ans = 0
            count = 0

            if add!=-1:
                u, v, w, index = add
                if find(u,parent) !=find(v,parent):
                    union(u, v)
                    ans += w
                    count += 1

            for u, v, w, index in edges:
                if skip==index or add==index:
                    continue

                if find(u,parent) != find(v,parent):
                    ans+=w
                    union(u,v)
                    count+=1
                if count==n-1:
                    break
            return ans if count == n - 1 else float('inf')


       

        mst=kruskal(edges,-1,-1)

        arr = [[], []]

        for u, v, w, index in edges:

            

            newmst = kruskal(edges,index,-1)

            if newmst > mst:
                arr[0].append(index)

            else:
                forced_mst = kruskal(edges,-1,[u,v,w,index])

                if forced_mst == mst:
                    arr[1].append(index)

        return arr
