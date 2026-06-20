class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        while n!=1:
            if n in seen:
                return False
            digit=0
            seen.add(n)
            while n > 0:
                digit += (n % 10)**2
                n //= 10
            n=digit
        return True
    