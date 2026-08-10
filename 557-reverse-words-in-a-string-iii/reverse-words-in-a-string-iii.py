class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        p=""
        for i in range(len(words)):
            p+=words[i][::-1]+" "
        return p.strip()
