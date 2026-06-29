class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp={}
        def rec(i,j):
            k=i+j
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            s_1=False
            s_2=False
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s1):
                if s3[k]==s1[i]:

                    s_1=rec(i+1,j)
            if j<len(s2):
                if s3[k]==s2[j]:

                    s_2=rec(i,j+1)
            dp[(i,j)]=s_1 or s_2 
            return dp[(i,j)]
        return rec(0,0) 
            

    
      


        