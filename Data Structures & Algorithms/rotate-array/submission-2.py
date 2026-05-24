class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def rev(arr,s,e):
            left=s
            right=e
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)
        return nums


        