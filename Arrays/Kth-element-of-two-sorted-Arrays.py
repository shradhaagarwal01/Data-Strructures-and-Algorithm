#Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
#The task is to find the element that would be at the k’th position of the final sorted array.
 
import sys
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            return self.kthElement(arr2,arr1,m,n,k)
        low = max(0,k-m)
        high = min(k,n)
        while low<=high:
            cut1 = (low+high)//2
            cut2 = k-cut1
            if cut1==0:
                l1 = -sys.maxsize
            else:
                l1 = arr1[cut1-1]
            if cut2==0:
                l2 = -sys.maxsize
            else:
                l2 = arr2[cut2-1]
            if cut1==n:
                r1 = sys.maxsize
            else:
                r1 = arr1[cut1]
            if cut2==m:
                r2 = sys.maxsize
            else:
                r2 = arr2[cut2]
            if(l1<=r2 and l2<=r1):
                return max(l1,l2)
            elif (l1> r2):
                high = cut1-1
            else:
                low = cut1+1
        return 1
