class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        INF=float("inf")
        dp={}
        def rec(i,j):
            if i>=n or j>=m:
                return INF
            if i==n-1 and j==m-1:
                return grid[i][j] 
            if (i,j) in dp :
                return dp[(i,j)]
            
            down=rec(i,j+1)+grid[i][j]
            right=rec(i+1,j)+grid[i][j]
            dp[(i,j)]=min(down,right)
            return dp[(i,j)]
        return rec(0,0)