# X : Sum which you need to search for 
    
def find3Numbers(arr, N, X):
    # Your Code Here
    arr.sort()
    i = 0
    target = 0
    while(i<N-2):
        target = X-arr[i]
        k = i+1
        j = N-1
        while(k<j):
            if arr[k]+arr[j] == target:
                return 1
            elif arr[k] + arr[j] > target:
                j = j-1
            else:
                k = k+1
        i = i+1
    return 0


t = int(input())
for i in range(t):
    n,sum=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    print(find3Numbers(a,n,sum))
