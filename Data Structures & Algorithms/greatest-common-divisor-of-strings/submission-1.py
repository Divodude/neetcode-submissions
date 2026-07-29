class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        if str1 + str2 != str2 + str1:
            return ""
        lensubs=math.gcd(len(str1),len(str2))
        if str1[:lensubs]==str2[:lensubs]:

            return str1[:lensubs]
        return ""