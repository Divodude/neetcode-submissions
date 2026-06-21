class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def rec(i,last):
            if i==n:
                return 0
            take=-100000
            if (i,last) in dp:
                return dp[(i,last)]
            if last<nums[i]:
                take=rec(i+1,nums[i])+1
            skip=rec(i+1,last)
            dp[(i,last)]=max(take,skip)
            return dp[(i,last)]
        return rec(0, float("-inf"))