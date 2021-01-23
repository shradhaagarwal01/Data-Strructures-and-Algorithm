def majorityElement(arr,N):
    #Your code here
    for i in range(len(arr)):
        if abs(N-arr[i]) in arr:
                return 1
    return -1




T=int(input())
while(T>0):
    L,N =[int(x) for x in input().strip().split()]
    A=[int(x) for x in input().strip().split()]
    print(majorityElement(A,N))
    T-=1

