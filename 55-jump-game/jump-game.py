from functools import cache

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        @cache  # Automatically handles memoization much faster than list lookups
        def solve(idx: int) -> bool:
            if idx >= n - 1:
                # Reached or overshot the last index
                return True
            
            # Extract max jump from current position
            max_jump = nums[idx]
            
            # Optimization: If max jump reaches or exceeds the end, stop immediately
            if idx + max_jump >= n - 1:
                return True
                
            # Check jump paths from largest to smallest (Greedy heuristic optimization)
            for i in range(max_jump, 0, -1):
                if solve(idx + i):
                    return True
                    
            return False

        return solve(0)
