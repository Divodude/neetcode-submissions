class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def check_dir(nums,idx):
            n=len(nums)
            if idx+1<n and nums[idx]==nums[idx+1]:
                if (idx)%2==0:
                    return 1
                else:
                    return -1
            elif idx-1>=0 and nums[idx-1]==nums[idx]:
                if (idx-1)%2==0:
                    return 1
                else:
                    return -1
            else:
                return 0
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if check_dir(nums,mid)==0:
                return nums[mid]
            elif check_dir(nums,mid)==-1:
                right=mid-1
            else:
                left=mid+1
        return -1

        

        