class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        nums.sort()

        def rec(sm):
            if sm==target:
                return 1 

            if sm>target:
                return 0
            if sm in dp :
                return dp[sm]
            ans=0
            for nm in nums:
                ans+=rec(sm+nm)
            dp[sm]=ans
            return dp[sm]
        return rec(0)
