#Given an array arr[] of distinct integers of size N and a value sum, 
#the task is to find the count of triplets (i, j, k), having (i<j<k) 
#with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.


class Solution:
    def countTriplets(self, arr, n, sum):
        #code here
        arr.sort()
        ans = 0
        for i in range(0,n-2):
            j = i + 1
            k = n-1
            while(j < k):
                if (arr[i]+arr[j]+arr[k] >=sum):
                    k = k-1
                else:
                    ans += (k - j)
                    j = j+1
        return ans
