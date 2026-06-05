class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        iland=0
        n=len(grid)
        m=len(grid[0])
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j):
            visit.add((i,j))
            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m and grid[newi][newj]=="1":
                    if (newi,newj) not in visit:
                        dfs(newi,newj)
        for i in range(n):
            for j in range(m):
                if (i,j) not in visit and grid[i][j]=="1":
                    iland+=1
                    dfs(i,j)
        return iland