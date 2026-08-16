class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
    
        changes=[]
        def settel(amount,changes):
            changes.sort(reverse=True)
            i = 0
            while i < len(changes):
                if changes[i] <= amount:
                    amount -= changes[i]
                    changes.pop(i)
                else:
                    i += 1
            if amount!=0:
                return False
            return True
        for i in bills:
            if i >5:
                if not settel(i-5,changes):
                    return False
            changes.append(i)
        return True
       