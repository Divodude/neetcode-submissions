class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n+2):
            idx=abs(nums[i])
            print(nums)
            if nums[idx]<0:
                return idx
            nums[idx]=-nums[idx]
        return 0