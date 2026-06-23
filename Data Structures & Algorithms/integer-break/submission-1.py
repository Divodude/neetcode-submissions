class Solution:
    def integerBreak(self, n: int) -> int:
        dp={}
        def rec( sm):
            if sm==n:
                return 1
            if sm>n:
                return 0
            ans=0
            if sm in dp:
                return dp[sm]
            for i in range(1,n):
                if i+sm<=n:
                    ans=max(rec(i+sm)*i,ans)
            dp[sm]=ans
            return dp[sm]
        return rec(0)
        