#naive approach

def isAnagram(s):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)
  
#using two dictionaries

def isAnagram(s):
    d1 = {}
    d2 = {}
    for i in s:
        d1[i] = d1.get(i,0)+1
    for i in t:
        d2[i] = d2.get(i,0)+1
    return d1==d2
            
#using single dictionary

class Solution:
    def isAnagram(s):
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        for i in t:
            if i not in d:
                return False
            else:
                d[i] = d.get(i,0)-1 
        for val in d.values():
            if val!=0:
                return False
        return True
