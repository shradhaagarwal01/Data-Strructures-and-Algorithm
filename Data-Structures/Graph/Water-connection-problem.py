#Every house in the colony has at most one pipe going into it and at most one pipe going out of it. 
#Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no 
#incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.
#Given two integers n and p denoting the number of houses and the number of pipes. 
#The connections of pipe among the houses contain three input values: ai, bi, di denoting the pipe of diameter di from house ai to house bi.
#Find the efficient way for the construction of the network of pipes.
#The output will contain the number of pairs of tanks and taps t installed in first line and the next t lines
#contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.


class Solution:
    def __init__(self):
        self.ans0 = 0
        self.ans1 = []
        self.ans2 = []
        self.ans3 = []
        self.rd1 = [0]*1100
        self.wt2 = [0]*1100
        self.cd3 = [0]*1100
        self.f_ans = []
        
    def dfs(self, w):
        if (self.cd3[w] == 0):
            return w
        if (self.wt2[w] < self.ans0):
            self.ans0 = self.wt2[w]
        return self.dfs(self.cd3[w])
        
    def solve(self, n, p ,a, b, d):
            
        i = 0
        
        while i < p:
            x = a[i]
            y = b[i]
            z = d[i]
            
            self.cd3[x] = y
            self.wt2[x] = z
            self.rd1[y] = x
            i += 1
            
        for j in range(1, n + 1):
            if self.rd1[j] == 0 and self.cd3[j]:
                 
                self.ans0 = 1000000000
                w = self.dfs(j)
                
                self.ans1.append(j)
                self.ans2.append(w)
                self.ans3.append(self.ans0)
                
        for i in range(len(self.ans1)):
            self.f_ans.append([self.ans1[i], self.ans2[i], self.ans3[i]])
            
        return self.f_ans
