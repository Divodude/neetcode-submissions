class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start,end):
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    end=mid
        
            return float("inf")
        n=len(nums)
        start=0
        end=n-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:

                end=mid

        rotation = start

        ans = bs(0, rotation - 1)

        if ans != float("inf"):
            return ans

        ans = bs(rotation, n - 1)

        if ans != float("inf"):
            return ans

        return -1
        