class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        pfx=1
        sfx=1
        ans=[0]*n

        for i in range(n):
            prefix[i]=pfx
            pfx*=nums[i]
        
        for j in range(n-1,-1,-1):
            print(sfx)
            suffix[j]=sfx
            
            sfx*=nums[j]
        print(suffix,prefix)
        for k in range(n):
            ans[k]=prefix[k]*suffix[k]
        return ans