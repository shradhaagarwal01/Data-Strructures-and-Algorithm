#Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. 
#If B cannot be a substring of A no matter how many times it is repeated, return -1.

class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        c = len(B)//len(A)
        a = (A*c)
        b = (A*(c+1))
        p = A*(c+2)
        if B in a:
            return c
        elif B in b:
            return c+1
        elif B in p:
            return c+2
        else:
            return -1
