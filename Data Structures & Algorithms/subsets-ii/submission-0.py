class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        nums.sort()
        def rec(i,arr):
            if i>=n:
                self.ans.append(arr.copy())
                return
            arr.append(nums[i])     
            rec(i+1,arr)
            arr.pop()
            j = i + 1
            while j < n and nums[j] == nums[i]: #basically skipping the duplicates nuber starting point to prevent dupilcate in the anser
                j += 1
            rec(j,arr)
        rec(0,[])
        return self.ans
        