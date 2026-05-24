class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        left=0
        right=n-1
        count=0

        while left<=right:
            remaining=limit
            if people[right]<=remaining:

                remaining-=people[right]
                right-=1
            
            if people[left]<=remaining:
                remaining-=people[left]
                left+=1
            count+=1
            
        return count