class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        
        def rec(i):
            if i==n:
                return 1
            if i>n:
                return 0
            if i in dp:
                return dp[i]
            one=rec(i+1)
            two=rec(i+2)
            dp[i]=one+two
            return dp[i]
        return rec(0)