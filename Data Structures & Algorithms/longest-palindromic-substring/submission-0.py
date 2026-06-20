class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand(l,r):
            st=""
            print(st)
            while l>=0 and r<n and s[l]==s[r]:
                st=s[l:r+1]
                l-=1
                r+=1
            return len(st),st
        ans=[]
        for i in range(n):
            ans.append(expand(i, i))      # odd length
            ans.append(expand(i, i + 1))
        ans.sort()
        return ans[-1][1]

        
            
            