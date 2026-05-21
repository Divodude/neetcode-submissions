class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict
        h_map= defaultdict(int)
        q=[]
        for i in nums:
            h_map[i]+=1
        for i in h_map:   
            heapq.heappush(q,(h_map[i],i))        
            if len(q)>k:
                heapq.heappop(q) 
        ans=[]
        print(q)
        for k in q:
            ans.append(k[1])
        return ans