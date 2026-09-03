class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        column=[]
        row=[]
        m=len( grid[0])
        n=len(grid)
        for i in grid:
            row.append( sum( i))
        for j in range(m):
            sm=0
            for i in range(n):
                sm+=grid[i][j]
            column.append(sm)
        ans=0
        for i in range(n):

            for j in range(m):
                if grid[i][j]:
                    if row[i]>1 or column[j]>1:
                        ans+=1
        return ans

            

                
