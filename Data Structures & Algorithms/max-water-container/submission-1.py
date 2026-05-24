class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        area=0
        while left<right:
            width=abs(left-right)
            ht=min(height[left],height[right])
            area=max(area,width*ht)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area        