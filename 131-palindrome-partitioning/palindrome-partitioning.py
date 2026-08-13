class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        temp=[]
        def backtrack(i):
            if i==n:
                ans.append(temp.copy())
            for j in range(i,n):
                subset=s[i:j+1]
                
                if subset == subset[::-1]:
                    temp.append(subset)
                    backtrack(j+1)
                    temp.pop()
        backtrack(0)
        return ans