class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        m=len(word1)
        n=len(word2) 
        i=0
        j=0   
        while i<m and j<n:
            result+=word1[i]
            result+=word2[j]
            j+=1
            i+=1
        if i<m:
            result+=word1[i:]
        if j<n:
            result+=word2[j:]
        
        return result
