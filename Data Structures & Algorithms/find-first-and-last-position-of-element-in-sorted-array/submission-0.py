class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums,target,lb):
            n=len(nums)
            left=0
            right=n-1
            idx=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    idx=mid
                    if lb:
                        right=mid-1
                    else:
                        left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return idx
        return [bs(nums,target,True),bs(nums,target,False)]


