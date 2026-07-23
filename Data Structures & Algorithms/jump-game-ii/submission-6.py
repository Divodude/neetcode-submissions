class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp={}
        def rec(idx):
            if idx >= n - 1:
                return 0

            if nums[idx] == 0:
                return float("inf")

            ans = float("inf")
            if idx in dp:
                return dp[idx]

            for jump in range(1, nums[idx] + 1):
                ans = min(ans, 1 + rec(idx + jump))
            dp[idx]=ans
            return ans

        return rec(0)