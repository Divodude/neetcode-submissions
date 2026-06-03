class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        def rec(i,c_sum,arr):
            if c_sum>target:
                return 
            if c_sum==target:
                self.ans.append(arr.copy())
                return 
            if i>=n:
                return 
            
            arr.append(nums[i])
            c_sum+=nums[i]
            rec(i,c_sum,arr)
            c_sum-=nums[i]
            arr.pop()
            rec(i+1,c_sum,arr)
        rec(0,0,[])
        return self.ans
        