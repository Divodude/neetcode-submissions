class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod=nums[0]
        n=len(nums)
        c_p=1
        for i in range(n):
            c_p*=nums[i]
            print(c_p)
            if c_p>min_prod:
                min_prod=c_p
            if nums[i]==0:
                c_p=1

        
        c_p=1
        for j in reversed(nums):
            c_p*=j
            if c_p>min_prod:
                min_prod=c_p
            if j==0:
                c_p=1
        return min_prod
            
    



            

        