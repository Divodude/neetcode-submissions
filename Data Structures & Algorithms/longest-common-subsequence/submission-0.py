class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        INF=float("inf")
        dp={}
        def rec(i,j):
            if i>=n or j>=m:
                return 0
 
            pick=-INF
            if (i,j) in dp :
                return dp[(i,j)]
            if text1[i]==text2[j]:
                pick=rec(i+1,j+1)+1
            right=rec(i+1,j)
            down=rec(i,j+1)
            dp[(i,j)]= max(pick,right,down)
            return dp[(i,j)]
        return rec(0,0)