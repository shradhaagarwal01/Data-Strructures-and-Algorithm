#Given a matrix of size N x M. You have to find the Kth element which will obtain while traversing the matrix spirally starting from the top-left corner of the matrix.

class Solution:
    def findK(self, matrix, m, n, p):
        # Your code goes here
        m = len(matrix)
        n = len(matrix[0])
        k = 0
        l = 0
        ans = []
        while(k<m and l<n): 
            for i in range(l,n):
                ans.append(matrix[k][i])
            k = k+1
            for i in range(k,m):
                ans.append(matrix[i][n-1])
            n = n-1
            if k<m:
                for i in range(n-1,l-1,-1):
                    ans.append(matrix[m-1][i])
                m = m-1
            if l<n:
                for i in range(m-1,k-1,-1):
                    ans.append(matrix[i][l])
                l = l+1
        return ans[p-1]
