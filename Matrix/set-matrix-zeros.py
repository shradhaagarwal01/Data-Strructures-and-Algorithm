class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, matrix):
        col0 = True
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(0,rows):
            if matrix[i][0] == 0:
                col0 = False
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
             
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 is False:
                matrix[i][0] = 0
