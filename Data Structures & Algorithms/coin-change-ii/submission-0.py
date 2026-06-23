class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp={}
        def rec(i,sm):
            if i >=n:
                return 0
            if sm>amount:
                return 0 
            if sm==amount:
                return 1
            if (i,sm) in dp:
                return dp[(i,sm)]
            take=rec(i,sm+coins[i])
            skip=rec(i+1,sm)
            dp[(i,sm)]=take+skip
            return dp[(i,sm)]
        return rec(0,0)
            
        