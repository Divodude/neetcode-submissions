class Solution:
    def isValid(self, s: str) -> bool:
        compliment={"(":")","[":"]","{":"}"}
        stack=[]

        for i in s:
            
            if stack and stack[-1] in compliment and  compliment[stack[-1]]==i:
                stack.pop()
                continue
            
            stack.append(i)
        if not stack:
            return True
        return False
