#Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.

from bisect import bisect_left as lower_bound
class Solution:
   def ValidPair(self, a, n):
       a = sorted(a)
       ans = 0
       for i in range(n):
           if (a[i] <= 0):
               continue 
           j = lower_bound(a, -a[i] + 1)
           ans += i - j
       return ans
