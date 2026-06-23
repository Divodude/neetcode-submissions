class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        INF=float("inf")
        n=len(stones)
        total=sum(stones)
        dp={}
        def rec(i,sm):
            if i==n:
                return abs(total-sm*2)
            if (i,sm) in dp :
                return dp[(i,sm)]
            take=rec(i+1,sm+stones[i])
            skip=rec(i+1,sm)
            dp[(i,sm)]=min(take,skip)
            return dp[(i,sm)]

        return rec(0,0)
            
