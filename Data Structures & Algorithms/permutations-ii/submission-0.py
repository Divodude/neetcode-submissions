class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        nums.sort()
        used=[False]*n
        def prem(i,arr):
            if len(arr)==n:
                self.ans.append(arr.copy())
                return

            for j in range(n):
                if j>0 and nums[j-1]==nums[j] and not used[j-1]:
                    continue   
                if used[j]:
                    continue
                used[j]=True
                arr.append(nums[j])
                prem(j+1,arr)
                arr.pop()
                used[j]=False
               
        prem(0,[])
        return self.ans