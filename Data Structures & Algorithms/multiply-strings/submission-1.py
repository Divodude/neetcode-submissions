class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def strtint(nums):
            pos=0
            num=0
            for i in nums[::-1]:
                num+=int(i)*10**pos
                pos+=1
            print(num)
            return num

        return f"{strtint(num1)*strtint(num2)}"
