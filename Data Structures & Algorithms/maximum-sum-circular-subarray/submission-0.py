class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)


        mx = float("-inf")
        sm = 0
        for x in nums:
            sm += x
            mx = max(mx, sm)
            if sm < 0:
                sm = 0

   
        if mx < 0:
            return mx

        mn = float("inf")
        sm = 0
        for x in nums:
            sm += x
            mn = min(mn, sm)
            if sm > 0:
                sm = 0

        return max(mx, total - mn)