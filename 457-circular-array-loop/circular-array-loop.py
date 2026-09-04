class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n=len(nums)
        def nexti(i):
            
            return (i+nums[i])%n
        for i in range(len(nums)):
            slow=i
            fast=i
            direction = nums[i] > 0
            while True:
                slow=nexti(slow)
                if slow==nexti(slow) or (nums[slow] > 0) != direction:
                    break
                fast=nexti(fast)
                if fast==nexti(fast) or (nums[fast] > 0) != direction:
                    break    
                fast=nexti(fast)
                if fast==nexti(fast) or (nums[fast] > 0) != direction:
                    break 
                
                
                if slow==fast :
                    return True
        return False