class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp={}
        def rec(alice,i,M):

            if i>=n:
                return 0 
            play=0
            skip=0
            res = 0 if alice else float("inf")
            total=0
            if (alice,i,M) in dp:
                return dp[(alice,i,M)]
            for X in range(1,2*M+1):

                if i+X>n:
                    break
                total+=piles[i+X-1]
                if alice:
                    res=max(res, total + rec(not alice, i + X, max(M, X)))
                else:
                    res = min(res, rec(not alice, i + X, max(M, X)))
            dp[(alice,i,M)]=res
            return dp[(alice,i,M)]
        return rec(True,0,1)
                