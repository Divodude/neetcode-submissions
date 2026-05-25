class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        n=len(nums)
        INF=float("inf")
        ans=INF
        sm=0
        for r in range(n):
            sm+=nums[r]
            while sm>=target:
                ans=min(ans,r-l+1)
                sm-=nums[l]
                l+=1
        if ans==INF:
            return 0
        return ans
            