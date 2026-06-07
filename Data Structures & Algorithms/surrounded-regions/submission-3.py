class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #boundary traversal
        coordinates=set() 
        
        n=len(board)
        m=len(board[0])
        visit=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
     
        def dfs(i,j):
            visit.add((i,j))
            coordinates.add((i,j))

            for di,dj in directions:
                newi,newj=di+i,dj+j
                if 0<=newi<n and 0<=newj<m and board[newi][newj]=="O":
                    if (newi,newj) not in visit:
                        
                        dfs(newi,newj)
        for i in range(n):
            if board[i][0]=="O":
                coordinates.add((i,0))
                if (i,0) not in visit:
                    dfs(i,0)
            if board[i][m-1]=="O":
                coordinates.add((i,m-1))
                if (i,m-1) not in visit:
                    dfs(i,m-1)
        
        for j in range(m):
            if board[0][j]=="O":
                coordinates.add((0,j))
                if (0,j) not in visit:
                    dfs(0,j)
            if board[n-1][j]=="O":
                coordinates.add((n-1,j))
                if (n-1,j) not in visit:
                    dfs(n-1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and  (i,j) not in coordinates:
                    board[i][j]="X"

    
            
                