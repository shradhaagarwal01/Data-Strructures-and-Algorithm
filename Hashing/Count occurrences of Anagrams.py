#Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.
import collections
class Solution:
	def search(self,p, s):
	    myDictP=collections.Counter(p)
        myDictS=collections.Counter(s[:len(p)])
        output=0
        i=0
        j=len(p)
        while j<=len(s):
            if myDictS==myDictP:
                output+=1

            myDictS[s[i]]-=1
            if myDictS[s[i]]<=0:
                myDictS.pop(s[i])
                
            if j<len(s):    
                 myDictS[s[j]]+=1
            j+=1
            i+=1
            
        return output 
