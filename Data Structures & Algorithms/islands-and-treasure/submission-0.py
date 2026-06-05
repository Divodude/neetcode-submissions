class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=float("inf")
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        que=[]
        visit=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    que.append((i, j,0))
                    visit.add((i,j))
        while que:
            i,j,dist=que.pop(0)
            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m and grid[newi][newj]!=-1:
                    if (newi,newj) not in visit:
                        grid[newi][newj]=dist+1   
                        que.append((newi,newj,dist+1))
                        visit.add((newi,newj))

