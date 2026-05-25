class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n=len(position)
        car=[]
        for i in range(n):
            car.append([position[i],speed[i]])
        car.sort()

        def can_fleet(i,j,end):
        
            p1,s1=car[i]
            p2,s2=car[j]

            if p1 == p2:
                return True

            if p1 > p2:
                front_pos, front_speed = p1, s1
                back_pos, back_speed = p2, s2
            else:
                front_pos, front_speed = p2, s2
                back_pos, back_speed = p1, s1

            if back_speed <= front_speed:
                return False

            t = (front_pos - back_pos) / (back_speed - front_speed)

            meet_pos = back_pos + back_speed * t

            return meet_pos <= end



        for i in range(n):
            while stack and can_fleet(stack[-1],i,target):
       
                stack.pop()
            stack.append(i)
        print(stack)
        return len(stack)

