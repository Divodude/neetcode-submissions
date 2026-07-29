from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)    
        formed = 0                

        l = 0
        ans = (float("inf"), 0, 0)

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

           
            if c in need and window[c] == need[c]:
                formed += 1

 
            while formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                left = s[l]
                window[left] -= 1

              
                if left in need and window[left] < need[left]:
                    formed -= 1

                l += 1

        if ans[0] == float("inf"):
            return ""

        return s[ans[1]:ans[2] + 1]