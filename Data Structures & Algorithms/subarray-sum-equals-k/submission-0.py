class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=[]
        pfx=0
        count=0
        for i in nums:
            pfx+=i
            prefix.append(pfx)
        from collections import defaultdict
        h_map=defaultdict(int)
        h_map[0]=1

            
        for p in prefix:
            if p-k in h_map:
                count+=h_map[p-k]
            h_map[p]+=1
        return count