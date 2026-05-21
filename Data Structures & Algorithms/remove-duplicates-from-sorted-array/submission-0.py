class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=float("inf")
        count=0
        left=0
        for i in nums:

            if i!=prev:
                nums[left]=i
                left+=1
                count+=1
            prev=i
        return count
                
        