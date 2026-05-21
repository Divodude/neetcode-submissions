class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merg(a,b):
            i,j=0,0
            ans=[]
            while i<len(a) and j<len(b):
                if a[i]<=b[j]:
                    ans.append(a[i])
                    i+=1
                else:
                    ans.append(b[j])
                    j+=1
            while i<len(a):
                ans.append(a[i])
                i+=1

            while j<len(b):
                ans.append(b[j])
                j+=1
            return ans
        def rec_sort(nums):
            print(nums)
            if len(nums)<=1:
                return nums
            
            left=rec_sort(nums[:len(nums)//2])
            right=rec_sort(nums[len(nums)//2:])
            return merg(left,right)
        return rec_sort(nums)