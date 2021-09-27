def occurance(arr,x):
    i = 0
    j = len(arr)-1
    ans1 = -1
    ans2 = -1
    for i in range(n):
        if arr[i]==x:
            ans1 = i
            break
    for j in range(n-1,-1,-1):
        if arr[j]==x:
            ans2 = j
            break
        
    return ans1,ans2
        
    



for t in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    if x not in arr:
        print(-1)
    else:
        ans1,ans2 = occurance(arr,x)
        print(ans1,ans2)
    
