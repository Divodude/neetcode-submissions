class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp={}
        def rec( i):
            if i>=n:
                return 0
            if i in dp:
                return dp[i]
   
            one =rec(i+1)
            two=rec(i+2)
            dp[i]=min(one,two)+cost[i]
            return  dp[i] 
        return min(rec(0), rec(1))