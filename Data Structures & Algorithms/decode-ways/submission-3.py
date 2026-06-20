class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)

        if s[0]=="0":
            return 0
        dp={}
        def rec(i):
            if i ==n:
                return 1
            if s[i]=="0":
                return 0 
            if i in dp:
                return dp[i]
            pick_one=rec(i+1)
            pick_two=0
            if i+1<n and 10<=int(s[i:i+2])<=26:
                pick_two=rec(i+2)
            dp[i]=pick_one+pick_two
            return dp[i]
        return rec(0)
        