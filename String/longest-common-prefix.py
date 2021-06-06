#Brute Force - Horizontal Scanning 

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs)==0:
        return ""
    prefix = strs[0]
    for i in range(1,len(strs)):
        while(prefix!=strs[i][:len(prefix)] and len(prefix)>0):
            prefix = prefix[0:-1]
    return prefix
    
#<------------------------------------------------------------------->
      
#Better - Vertical Scanning

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs)==0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1,len(strs)):
            if i==len(strs[j]) or strs[j][i]!=c:
                return strs[0][:i]
    return strs[0]
      
#<------------------------------------------------------------------->

#Optimal - By sorting 

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs)==0:
        return ""
    strs.sort()
    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i]!=strs[-1][i]:
            break
        prefix = prefix+strs[0][i]
    return prefix
