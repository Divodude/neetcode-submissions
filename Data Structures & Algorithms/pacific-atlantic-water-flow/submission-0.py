class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pf=set()
        at=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(heights)
        m=len(heights[0])
        def dfs(i,j,visit,flag):
            if flag:
                pf.add((i,j))
            else:
                at.add((i,j))
            
            visit.add((i,j))

            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m and heights[i][j]<=heights[newi][newj]:
                    if (newi,newj) not in visit:
                        dfs(newi,newj,visit,flag)
        #pacific
        for i in range(n):
            dfs(i,0,set(),True)
        for j in range(m):
            dfs(0,j,set(),True)
        #atlantic
        
        for i in range(n):
            dfs(i,m-1,set(),False)
        for j in range(m):
            dfs(n-1,j,set(),False)
        
        return list(pf.intersection(at))




        

        