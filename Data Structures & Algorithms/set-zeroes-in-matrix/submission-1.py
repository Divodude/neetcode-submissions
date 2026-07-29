class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ycoord=set()
        xcoord=set()
        m=len(matrix)
        n=len(matrix[0])
        zero=[ 0 ]*n
        for i in range( m):
            for j in range(n):
                if matrix[i][j]==0:
                   
                    ycoord.add(j)
                    xcoord.add(i)
        
        for i in range(m):
            for j in ycoord:
                matrix[i][j]=0
            for k in xcoord:
                matrix[k]=zero

     

        
        