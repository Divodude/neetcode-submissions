class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        self.area=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)
        m=len(grid[0])

        def dfs(i,j):

            visit.add((i,j))
            for di,dj in directions:
                newi,newj=i+di,j+dj

                if 0<=newi<n and 0<=newj<m:
                    if (newi,newj) not in visit:
                    
                        if grid[newi][newj]==0:
                            self.area+=1
                        else:
                        
                            dfs(newi,newj)
                else:
                    self.area+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in visit:
                    dfs(i,j)
                    
        return self.area
        