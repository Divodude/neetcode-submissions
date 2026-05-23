class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map=set(nums)
        candidates=[]
        ans=0

        for i in nums:
            if i-1 not in h_map:
                candidates.append(i)#possible start point 
        for j in candidates:
            temp=j
            count=0
            while temp in h_map:
                count+=1
                temp+=1
            ans=max(ans,count)
        return ans
            
        