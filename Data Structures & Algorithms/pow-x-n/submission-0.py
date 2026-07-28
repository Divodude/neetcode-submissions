class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        def mul(n):
            if n==0:
                return 1
            fh=mul(n//2)
            if n%2==0:
                return fh*fh
            else:
                return fh*fh*x
            
        return mul(n)
