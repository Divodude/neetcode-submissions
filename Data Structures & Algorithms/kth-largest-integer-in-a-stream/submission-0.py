class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.que = []
        for i in nums:
            heapq.heappush(self.que,i)
            if len(self.que)>self.limit:
                heapq.heappop(self.que)


        

    def add(self, val: int) -> int:
        heapq.heappush(self.que,val)
        if len(self.que)>self.limit:
            heapq.heappop(self.que)
        return self.que[0]



        
