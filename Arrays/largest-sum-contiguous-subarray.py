#Kadane's Algorithm (Very Important)
#Algorithm Paradigm : Dynamic Programming
def maxSubArraySum(arr,n):
    max = 0
    end = 0
    for i in range(n):
        end = end+arr[i]
        if end<0:
            end = 0
        elif max<end:
            max = end
    return max
    


n=int(input())
arr=[int(x) for x in input().strip().split()]
print(maxSubArraySum(arr,n))
