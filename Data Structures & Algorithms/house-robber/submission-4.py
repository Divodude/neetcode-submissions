class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def rec( i):
            if i >=n:
                return 0
            if i in dp :
                return dp[i]
            rob=rec(i+2)+nums[i]
            skip=rec(i+1)+0
            dp[i]=max(rob,skip)
            return dp[i]
        return rec(0)
        