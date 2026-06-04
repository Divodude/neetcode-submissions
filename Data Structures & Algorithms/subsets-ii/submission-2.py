class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        nums.sort()

        def rec(i,arr):
            
            
            self.ans.append(arr.copy())
                 
            for j in range(i,n):
                if j>i and  nums[j-1]==nums[j]:
                    continue

                arr.append(nums[j])     
                rec(j+1,arr)
                arr.pop()
     
        rec(0,[])
        return self.ans
        