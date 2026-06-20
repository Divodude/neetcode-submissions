class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = {}

        def rec(i, end):
            if i > end:
                return 0

            if (i, end) in dp:
                return dp[(i, end)]

            rob = nums[i] + rec(i + 2, end)
            skip = rec(i + 1, end)

            dp[(i, end)] = max(rob, skip)
            return dp[(i, end)]

        return max(rec(0, n - 2), rec(1, n - 1))