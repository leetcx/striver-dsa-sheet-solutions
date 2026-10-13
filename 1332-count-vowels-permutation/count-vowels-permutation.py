class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels=["a","e","i","o","u"]
        dp={}
        def count(n,prev):
            if n==0:
                return 1
            
            state=(n,prev)
            if state in dp:
                return dp[state]
            skip=0
            take=0
            for i in range(len(vowels)):
                if prev == "#":
                    take += count(n - 1, vowels[i])
                elif vowels[i] == "a" and prev == "e":
                    take += count(n - 1, vowels[i])
                elif vowels[i] == "e" and (prev == "a" or prev == "i"):
                    take += count(n - 1, vowels[i])
                elif vowels[i] == "i" and prev != "i":
                    take += count(n - 1, vowels[i])
                elif vowels[i] == "o" and (prev == "i" or prev == "u"):
                    take += count(n - 1, vowels[i])
                elif vowels[i] == "u" and prev == "a":
                    take += count(n - 1, vowels[i])
           

            dp[state]= take
            return dp[state] % ((10**9)+7)
        return count(n,"#") % ((10**9)+7)
            
