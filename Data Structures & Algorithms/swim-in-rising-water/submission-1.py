class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:


        import heapq
        n=len(grid)
        m=len(grid[0])
        cost=grid[0][0]

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        que=[(0,0,0)]
        visit=set()
        while que:
            w,i,j=heapq.heappop(que)
            cost=max(w,cost)
            if i==n-1 and j==m-1:
                return cost

            for di,dj in directions:
                newi,newj=i+di,j+dj
                if 0<=newi<n and 0<=newj<m:
                    if (newi,newj) not in visit:
                        heapq.heappush(que,(grid[newi][newj],newi,newj))
                        visit.add((newi,newj))
        return cost


        