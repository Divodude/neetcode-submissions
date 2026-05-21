class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        def swap(a,b):
            return b,a
        def merg(nums1,nums2):
            i=0
            j=0
            if n<=0:
                return 
            while i<m:
   
                if  nums1[i]<=nums2[0]:
                    i+=1
                else:
                    nums1[i],nums2[0]=swap(nums1[i],nums2[0])
                    nums2.sort()
                    
                    j+=1
            j=0
            while j<n:
                nums1[i]=nums2[j]
                i+=1
                j+=1
        merg(nums1,nums2)

