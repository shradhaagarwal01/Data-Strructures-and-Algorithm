#Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

class Solution:
	def overlappedInterval(self, arr):
		arr = sorted(arr, key=lambda x: x[0])
        ans = [arr[0]]
        for i in range(1,len(arr)):
            if ans[-1][1]>=arr[i][0]:
                ans[-1][1] = max(ans[-1][1],arr[i][1])
            else:
                ans.append(arr[i])
        return ans
		
