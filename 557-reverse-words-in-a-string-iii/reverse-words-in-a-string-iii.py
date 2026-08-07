class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        word=s.split()
        n=len(word)
        for i in range(n):
            p=word[i][::-1]
            ans+=p+" "
        return ans.strip()


