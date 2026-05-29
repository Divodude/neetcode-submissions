class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a,b):
            return -(a*a+b*b)**0.5
        import heapq
        que=[]
        ans=[]
        for i in points:
            heapq.heappush(que,(distance(i[0],i[1]),[i[0],i[1]]))
            if len(que)>k:
                heapq.heappop(que)
            
        for k in que:
            print(k)
            ans.append(k[1])
        return ans
        