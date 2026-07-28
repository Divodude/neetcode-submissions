class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        def merg(a,b):
            return [min(a[0],b[0]),max(a[1],b[1])]
        ans=[]    
        for ivl in intervals:
            if not ans:
                ans.append(ivl)
            elif ans[-1][1]>=ivl[0]:
                ans[-1]=merg(ans[-1],ivl)
            else:
                ans.append(ivl)
        return ans

            
        