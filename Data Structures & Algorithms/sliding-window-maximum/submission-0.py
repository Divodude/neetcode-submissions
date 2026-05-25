class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        start=0
        end=k-1
        ans=[]
        while end<n:
            ans.append(sorted(nums[start:end+1],reverse=True)[0])
            end+=1
            start+=1
        return ans
        


            

        