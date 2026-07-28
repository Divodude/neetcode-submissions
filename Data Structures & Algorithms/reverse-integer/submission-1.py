class Solution:
    def reverse(self, n: int) -> int:
        rev = 0
        x = abs(n)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow BEFORE updating rev
            if rev > 214748364:
                return 0

            if rev == 214748364:
                if (n >= 0 and digit > 7) or (n < 0 and digit > 8):
                    return 0

            rev = rev * 10 + digit

        return -rev if n < 0 else rev
        