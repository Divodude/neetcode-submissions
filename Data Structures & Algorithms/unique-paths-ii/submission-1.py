class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        def rec(i,j):
            
            if i>=m or j>=n:
                return 0 
            if i==m-1 and j==n-1:
                return 1
            if obstacleGrid[i][j]==1:
                return 0 
            if (i,j) in dp :
                return dp[(i,j)]
            down=rec(i+1,j)
            right=rec(i,j+1)
            dp[(i,j)]=down+right
            return dp[(i,j)]
        return rec(0,0)