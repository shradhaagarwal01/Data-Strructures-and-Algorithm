#Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:
#Insert a character at any position of the string.
#Remove any character from the string.
#Replace any character from the string with any other character.


def edit(s,t,m,n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    
            elif j == 0:
                dp[i][j] = i    
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) 
    return dp[m][n]
        
class Solution:
	def editDistance(self, s, t):
		return edit(s,t,len(s),len(t))
