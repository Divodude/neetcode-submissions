class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        n=len(nums)
        h_map={}
        nums.sort()
        for i in range(n):
            for j in range(i,n):
                comliment=(nums[i]+nums[j])
                if -comliment in h_map and i!=j :
                    ans.append((nums[i],nums[j],-comliment))
            h_map[nums[i]]=i
        return list(set(ans))
                
        