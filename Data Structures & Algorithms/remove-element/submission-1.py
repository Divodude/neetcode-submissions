class Solution:
    def removeElement(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        def swap(a,b):
            return b,a
        while left<=right:
            print(nums)
            if nums[left]!=k:
                left+=1
            else:
                nums[left],nums[right]=swap( nums[left],nums[right])
                right-=1

                
        count=0
        for i in nums:
            if i !=k:
                count+=1
        return count 
