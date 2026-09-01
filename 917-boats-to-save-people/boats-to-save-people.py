class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low=0
        high=len(people) -1
        boat=0
        while low<=high:
            if people[low]+people[high]<=limit:
                boat+=1
                low+=1
                high-=1
            else:
                boat+=1
                high-=1
        return boat
