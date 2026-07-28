class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[]
        def merg(a,b):
            return [min(a[0],b[0]),max(a[1],b[1])]
    
        for ivl in intervals:
            if not ans:
                ans.append(ivl)
            elif ivl[0]<=ans[-1][1]:

                ans[-1]=merg(ans[-1],ivl)
            else:
                ans.append(ivl)
        return ans
            

