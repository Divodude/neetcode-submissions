class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visit=set()
        self.ans=False
        n=len(board)
        m=len(board[0])

        def dfs(i,j,s):
            visit.add((i,j))
            if self.ans:
                visit.remove((i,j))
                return 
            
            
            if s==word:
                self.ans=True
                visit.remove((i,j))
                return 
            if len(s) > len(word):
                visit.remove((i,j))
                return
            
            for di,dj in directions:
                newi=i+di
                newj=j+dj

                if 0<=newi<n and 0<=newj<m:
                    if (newi,newj) not in visit:
                        dfs(newi, newj, s + board[newi][newj])
            visit.remove((i,j))
        for i in range(n):
            for j in range(m):
                if (i,j) not in visit:
                    
                    dfs(i,j,board[i][j])
                    if self.ans:
                        return True
        return False

                    