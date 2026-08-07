class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max=0
        ans=""
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n:
                if s[left]==s[right]:
                    if right-left+1>len(ans):
                        ans=s[left:right+1]
                    left-=1
                    right+=1
                else:
                    break

            left=i
            right=i+1
            while left>=0 and right<n:
                if s[left]==s[right]:
                    if right-left+1>len(ans):
                        ans=s[left:right+1]
                    left-=1
                    right+=1
                else:
                    break
        return ans

                