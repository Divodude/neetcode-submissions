class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def can_collide(a, b):
            return a > 0 and b < 0
        stack=[]
        n=len(asteroids)

        for i in range(n):
            
            while stack and can_collide(stack[-1],asteroids[i]) and abs(stack[-1])<abs(asteroids[i]):
                stack.pop()
            if stack and can_collide(stack[-1],asteroids[i]) and  abs(stack[-1])==abs(asteroids[i]):
                stack.pop()
                continue
            if stack and can_collide(stack[-1],asteroids[i]) and abs(stack[-1])>abs(asteroids[i]):
                continue
            stack.append(asteroids[i])
        return stack 



        