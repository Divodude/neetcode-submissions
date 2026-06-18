class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq 
        que=[(0,0)]
        n=len(points)
        cost=0
        tree=set()
        def man(i,j):
            return abs(i[0]-j[0])+abs(j[1]-i[1])
        while len(tree)<n :
            w,node=heapq.heappop(que)
            if node in tree:
                continue
            cost+=w
            tree.add(node)

            for nei in range(n):
                if nei not in tree:
                    dis = man(points[node], points[nei])
                    heapq.heappush(que, (dis, nei))
        return cost

