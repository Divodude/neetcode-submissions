"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals = sorted(intervals, key=lambda x: x.start)
        prev=[]
        for ivl in intervals:
            if not prev:
                prev=[ivl.start,ivl.end]
            elif prev[1]>ivl.start:
                return False
            
            prev=[ivl.start,ivl.end]
        return True
