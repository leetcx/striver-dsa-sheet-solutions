class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        temp=[]
        ans=[]
        def all(i):
            nonlocal ans
            nonlocal temp
            if len(temp)==k:
                ans.append(temp.copy())
                return
            if i>=n+1:
                return
           
            temp.append(i)
            all(i+1)
            temp.pop()
            all(i+1)
        all(1)
        return ans