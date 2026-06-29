class Solution:
    def canJump(self, nums: List[int]) -> bool:


        n=len(nums)
        dp={}
        import sys
        sys.setrecursionlimit(10**6)
        def rec(i):
            if i>=n-1:
                return True
            if i in dp:
                return dp[i]
            for j in range(1, min(nums[i], n - 1 - i) + 1):
                if rec(i+j):
                    dp[i]=True
                    return True
            dp[i]=False
            return False
        return rec(0)




