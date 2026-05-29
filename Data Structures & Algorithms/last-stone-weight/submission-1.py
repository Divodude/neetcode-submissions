class Solution:
    def lastStoneWeight(self, que: List[int]) -> int:
        import heapq 
        lw=0
        que= [-x for x in que]

        heapq.heapify(que)
        print(que)
        while len(que)>=2:
            lw=-heapq.heappop(que)
            cw=-heapq.heappop(que)
            if lw==cw:
                continue
            elif lw>cw:
                heapq.heappush(que, -(lw - cw))
            else:
                lw=cw
        print(que)
        if que:
            return -que[0]

        else:
            return 0
            

        