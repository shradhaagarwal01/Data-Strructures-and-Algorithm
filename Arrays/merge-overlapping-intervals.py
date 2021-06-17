# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
 
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, arr):
        if len(arr)==0 or len(arr)==1:
            return arr
        arr.sort(key = lambda x: x.start)
        m = Interval(arr[0].start,arr[0].end)
        ans = []
        for i in range(1,len(arr)):
            if m.end>=arr[i].start:
                m.end = max(m.end,arr[i].end)
            else:
                ans.append(m)
                m = Interval(arr[i].start,arr[i].end)
        ans.append(m)
        return ans
