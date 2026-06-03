class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        n=len(nums)
        def rec(i,arr):
            if i>=n:
                self.ans.append(arr.copy())
                return 
            arr.append(nums[i])
            rec(i+1,arr)
            arr.pop()
            rec(i+1,arr)
            
             
        rec(0,[])
        return self.ans
            

        