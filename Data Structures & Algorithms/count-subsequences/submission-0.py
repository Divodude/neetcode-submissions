class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp={}
        def rec(i,j):
            if j>=m:
                return 1
            if i==n:
                return 0
            fwd=0
            if (i,j) in dp :
                return dp[(i,j)]
            if s[i]==t[j]:
                fwd=rec(i+1,j+1)
            nfwd=rec(i+1,j)
            dp[(i,j)]=nfwd+fwd
            return dp[(i,j)]
        return rec(0,0)