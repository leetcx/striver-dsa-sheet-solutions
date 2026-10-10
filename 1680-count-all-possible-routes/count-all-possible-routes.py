class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        dp={}
        def count(i, fuel):
            if fuel < 0:
                return 0
            state=(i,fuel)
            if state in dp:
                return dp[state]

            take = 1 if i == finish else 0

            for j in range(len(locations)):
                if i != j:
                    cost = abs(locations[i] - locations[j])
                    if fuel >= cost:
                        take += count(j, fuel - cost)

            dp[state]= take % (10**9 + 7) 
            return dp[state]  
        return count(start,fuel) 