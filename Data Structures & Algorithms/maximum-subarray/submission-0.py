class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=0
        ans=float("-inf")
        for i in nums:
            sm+=i
            ans=max(ans,sm)
            if sm<0:
                sm=0
        return ans
        