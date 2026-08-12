class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        temp=[]

        def backtrack(i,n):
            if n==0 and len(temp)==k :
                ans.append(temp.copy())
            if n<0 or i>9 or len(temp)>=k :
                return 
            for j in range(i,10):
                if j>i and j==i:
                    continue
                temp.append(j)
                backtrack(j+1,n-j)
                temp.pop()
        backtrack(1,n)
        return ans