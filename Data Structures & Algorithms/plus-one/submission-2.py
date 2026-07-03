class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        i = len(digits) - 1
        carry = 1

        while i >= 0 and carry:
            total = digits[i] + carry
            carry = total // 10
            digits[i] = total % 10
            i -= 1

        if carry:
            digits.insert(0, 1)

        return digits