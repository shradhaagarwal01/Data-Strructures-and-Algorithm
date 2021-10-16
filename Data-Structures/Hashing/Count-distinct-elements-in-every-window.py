#Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

class Solution:
    def countDistinct(self, A, N, B):
        # Code here
        res=[]
        dic={}
        for i in range(B):
            if A[i] in dic:
                dic[A[i]]+=1
            else:
                dic[A[i]]=1
        res.append(len(dic))
        for j in range(1,len(A)-B+1):
            if dic[A[j-1]]==1:
                dic.pop(A[j-1])
            else:
                dic[A[j-1]]-=1
            if A[j+B-1] in dic:
                dic[A[j+B-1]]+=1
            else:
                dic[A[j+B-1]]=1
            res.append(len(dic))
        return res
