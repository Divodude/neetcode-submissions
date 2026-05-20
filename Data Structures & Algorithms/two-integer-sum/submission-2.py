class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        h_map=defaultdict(int)
        n=len(nums)
        for i in range(n):
            if target-nums[i] in h_map:
                id1=min(i,h_map[target-nums[i]])
                id2=max(i,h_map[target-nums[i]])
                return [id1,id2]
            h_map[nums[i]]=i





        