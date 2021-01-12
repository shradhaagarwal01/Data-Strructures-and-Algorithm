#Dutch National Flag Algorithm or 3-way Partitioning Alogrithm
def sort012(arr,n):
    i = 0
    j = 0
    k = n-1
    while(j<=k):
        if arr[j]==0:
            arr[j],arr[i] = arr[i],arr[j]
            j = j+1
            i = i+1
        elif arr[j]==2:
            arr[j],arr[k] = arr[k],arr[j]
            k = k-1
        else:
            j = j+1
            

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    sort012(arr,n)
    for i in arr:
        print(i, end=' ')
    print()