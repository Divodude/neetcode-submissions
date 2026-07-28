class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev=[]
        count=0
        for ivl in intervals:
            if not prev:
                prev=ivl
            elif ivl[0]<prev[1]:
                count+=1
                if ivl[1]<prev[1]:
                    prev=ivl
            else:
                prev=ivl
        return count