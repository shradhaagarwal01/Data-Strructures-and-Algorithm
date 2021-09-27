#Iterative
class Solution:
    def countAndSay(self, n):
        ret = "1"
        for _ in range(n-1):
            ret = self.nextStep(ret)
        return ret
    
    def nextStep(self,prev):
        res = ""
        i = 0
        while(i<len(prev)):
            c = 1
            while (i+1)<len(prev) and prev[i]==prev[i+1]:
                i = i+1
                c = c+1
            res = res+str(c)+prev[i]
            i = i+1
        return res
       
#Reursive
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prev = self.countAndSay(n-1)
        res = ""
        i = 0
        while(i<len(prev)):
            c = 1
            while (i+1)<len(prev) and prev[i]==prev[i+1]:
                i = i+1
                c = c+1
            res = res+str(c)+prev[i]
            i = i+1
        return res
        
