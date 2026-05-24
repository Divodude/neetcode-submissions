class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map={}
        n=len(nums)
        for i in range(n):
            if nums[i] in h_map :
                if abs(i-h_map[nums[i]])<=k:
                    return True
            h_map[nums[i]]=i
        return False
