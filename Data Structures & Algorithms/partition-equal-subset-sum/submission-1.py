class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2!=0:
            return False
        target=sm//2
        n=len(nums)
        dp={}
        def rec(i,sm):
            if sm==target:
                return True
            if sm>target:
                return False
            if i>=n:
                return False
            if (i,sm) in dp :
                return dp[(i,sm)]

            pick=rec(i+1,sm+nums[i])
            skip=rec(i+1,sm)
            dp[(i,sm)]=pick or skip
            return dp[(i,sm)]
        return rec(0,0)
            
        