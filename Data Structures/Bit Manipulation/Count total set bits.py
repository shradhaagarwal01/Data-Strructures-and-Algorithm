#You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

def solve(n):
    x = 0
    while((1<<x)<=n):
        x = x+1
    return x-1
    
    
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        if n<=1:
            return n
        x = solve(n)
        count = (1<<(x-1))*x + (n-(1<<x)+1) + self.countSetBits(n-(1<<x))
        return count
