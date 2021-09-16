
#There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
#What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

#Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

class Solution:
    def maximumMeetings(self,n,start,end):
        ans = []
        sortedArr = []
        for i in range(n):
            a = []
            a.append(start[i])
            a.append(end[i])
            a.append(i)
            sortedArr.append(a)
        sortedArr.sort(key=lambda x:x[1])
        ans.append(sortedArr[0][2])
        i = 0
        for j in range(1,n):
            if sortedArr[j][0]>sortedArr[i][1]:
                ans.append((sortedArr[j][2])+1)
                i = j
        return len(ans)
