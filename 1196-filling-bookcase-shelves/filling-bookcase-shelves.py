class Solution:
    def minHeightShelves(self, books: list[list[int]], shelf: int) -> int:
        dp={}
        def mini(i,width,maxiii):
            if i>=len(books):
                return maxiii
            state=(i,width,maxiii)
            if state in dp:
                return dp[state]
            
            if width+books[i][0]>shelf:
                ans=maxiii+mini(i+1,books[i][0],books[i][1])
                dp[state]= ans
                return ans
            else:
                ans=maxiii+mini(i+1,books[i][0],books[i][1])
                continue1=mini(i+1,width+books[i][0],max(maxiii,books[i][1]))
                
                dp[state]= min(ans,continue1)
                return dp[state]
        return mini(0,0,0)

            