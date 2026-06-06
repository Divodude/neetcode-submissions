class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visit=set()
        que=[]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        result=0
        for i in range(n):
            for j  in range(m):

                if (i,j) not in visit and grid[i][j]==2:
                    que.append((i,j,0))

        while que:
            ql=len(que)
            for _  in range(ql):

                i,j,t=que.pop(0)
                result=max(result,t)
                for di,dj in directions:
                    newi,newj=di+i,dj+j
                    if 0<=newi<n and 0<=newj<m and grid[newi][newj]==1:
                        if  (newi,newj) not in visit:
                            grid[newi][newj]=2
                            que.append((newi,newj,t+1))
                            visit.add((newi,newj))
            print(grid)
        for i in range(n):
            for j  in range(m):

                if  grid[i][j]==1:
                    return -1
        return result


        