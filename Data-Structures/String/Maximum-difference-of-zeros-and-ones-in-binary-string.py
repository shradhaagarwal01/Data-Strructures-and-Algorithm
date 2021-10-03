#Given a binary string S consisting of 0s and 1s. 
#The task is to find the maximum difference of the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a string.
#Note: In the case of all 1s, the answer will be -1.


class Solution:
	def maxSubstring(self, S):
		sm = 0
		maxi = 0
		for i in range(0,len(S)):
		    sm += (1 if S[i] == '0' else -1)
		    if sm<0:
		        sm = 0
		    maxi = max(maxi,sm)
		if maxi==0:
		    return -1
		return maxi
