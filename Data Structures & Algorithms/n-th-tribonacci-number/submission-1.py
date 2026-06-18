class Solution:
    def tribonacci(self, n: int) -> int:
        dp={}
        def trib(i):
            if i==1 or i==2:
                return 1
            if i==0:
                return 0
            if i in dp:
                return dp[i]
            dp[i]=trib(i-1)+trib(i-2)+trib(i-3)
            return dp[i]
        return trib(n)
             
        