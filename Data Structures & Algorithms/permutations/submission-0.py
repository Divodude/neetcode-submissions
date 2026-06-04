class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        def prem(i,arr):
            if len(arr)==n:
                self.ans.append(arr.copy())
                return

            for j in range(n):   
                if nums[j] in arr:
                    continue         
                arr.append(nums[j])
                prem(j+1,arr)
                arr.pop()
               
        prem(0,[])
        return self.ans
        