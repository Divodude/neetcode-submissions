class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        
        def dfs(i,j):
            visit.add((i,j))
            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m and grid[newi][newj]==1:
                    if (newi,newj) not in visit:
                        self.area+=1
                        dfs(newi,newj)
        result=0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visit and grid[i][j]==1:
                    self.area=1
                    dfs(i,j)
                   
                    result=max(result,self.area)
        return result

        