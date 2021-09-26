def rotate(arr,n):
    temp = arr[n-1]
    i = n-1
    while(i!=0):
        arr[i] = arr[i-1]
        i = i-1   
    arr[0] = temp
    return arr     
    
    

n=int(input())
arr=list(map(int,input().strip().split()))
arr = rotate(arr,n)
print(*arr)
        
