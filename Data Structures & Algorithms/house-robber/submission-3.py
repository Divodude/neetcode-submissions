class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def rec(i,lr):
            if i>=n:
                return 0
            rob=-1
            not_rob=-1
            if (i,lr) in dp:
                return dp[(i,lr)]
            if i-1!=lr:
                
                rob=rec(i+1,i)+nums[i]
            not_rob=rec(i+1,lr)+0
            dp[(i,lr)]=max(rob,not_rob)
            return dp[(i,lr)]
        return rec(0,-2)

            

        