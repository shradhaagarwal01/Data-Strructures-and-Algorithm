class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        d = {}
        for i in range(1,len(A)+1):
            d[i]=0
        for i in range(0,len(A)):
            d[A[i]] = d.get(A[i])+1
        for i in d:
            if d[i]==0:
                b = i
            if d[i] == 2:
                a = i
        return a,b
