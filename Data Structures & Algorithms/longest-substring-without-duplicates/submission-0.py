class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        n=len(s)
        l=0
        ans=0
        for r in range(n):
        
            while s[r] in seen and l<=r:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            ans=max(ans,r-l+1)
        return ans 