def subset(arr1,arr2):
    if len(arr2) > len(arr1):
        return False
    for i in range(len(arr2)):
        if arr2[i] not in arr1:
            return False
            
    return True

for t in range(int(input())):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    ans = subset(arr1,arr2)
    if ans:
        print("Yes")
    else:
        print("No")