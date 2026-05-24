
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        new_s=""
        nu = set(string.ascii_letters + string.digits)
        for j in s:
            if j not in nu:
                continue
            new_s+=j.lower()
        
            

        def rev(s):
            s = list(s)   

            left = 0
            right = len(s) - 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            return "".join(s) 
        return new_s == rev(new_s)

            

        
        