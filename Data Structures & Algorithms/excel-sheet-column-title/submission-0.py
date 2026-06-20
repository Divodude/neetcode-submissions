class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mp = {chr(ord('A') + i): i + 1 for i in range(26)}
        ans=""
        n=columnNumber
        while n:
            n -= 1
            ans += chr(ord('A') + n % 26)
            n //= 26
        return ans[::-1]