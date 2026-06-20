class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        INF=float("inf")
        dp={}
        def rec(i,amount):
            if amount==0:
                return 0 
            if i>n-1:
                return INF
            if amount<0:
                return INF
            if (i,amount) in dp :
                return dp[(i,amount)]
            pick_same=INF
            if amount-coins[i]>=0:
                pick_same=rec(i,amount-coins[i])+1
            skip=rec(i+1,amount)+0
            dp[(i,amount)]=min(pick_same,skip)
            return  dp[(i,amount)]
        ans=rec(0,amount)
        if ans!=INF:
            return ans
        else:
            return -1
        