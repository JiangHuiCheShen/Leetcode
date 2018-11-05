class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return []
        intervals.sort()
        start=intervals[0].start
        end=intervals[0].end
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i].start>end:
                ans.append([start,end])
                start=intervals[i].start
                end=intervals[i].end
            else:
                end=intervals[i].end
        ans.append([start,end])
        return ans

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

a=Solution()
b=a.merge([Interval(1,4),Interval(1,5)])