#You are given an array arr[] of n integers and q queries in an array queries[] of length 2*q containing l, r pair for all q queries. 
#You need to compute the following sum over q queries.
#sum(l,r) = arr[l]+arr[l+1]....+arr[r]
#Array is 1-Indexed.

class Solution:
    def querySum(self, n, arr, q, queries):
        ans = []
        for i in range(0,len(queries),2):
            l = queries[i]
            r = queries[i+1]
            tot = 0
            while l-1<=r-1:
                tot = arr[l-1]+tot
                l=l+1
            ans.append(tot)
        return ans
                
