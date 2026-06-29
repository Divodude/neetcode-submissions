class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        n=len(matrix)
        m=len(matrix[0])
        dp={}
        def dfs(i,j):
            if i>=n or j>=m or i<0 or j<0 :
                return 0
            
            res=1
            if (i,j) in dp:
                return dp[(i,j)]

            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m:
                    if matrix[i][j]<matrix[newi][newj]:
                        res=max(dfs(newi,newj)+1,res)
            dp[(i,j)]=res
            return dp[(i,j)]
        ans=1
        for i in range(n):
            for j in range(m):

                ans=max(ans,dfs(i,j))
        return ans
                      
            
                        
