class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def rec(i,sm):

            if i>=n:
                if sm==target:
                    return 1
                else:
                    return 0
                
            a=0
            s=0

                
            a=rec(i+1,sm+nums[i])
            s=rec(i+1,sm-nums[i])
            return a+s
        return rec(0,0)
            