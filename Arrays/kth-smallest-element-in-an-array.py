def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    return arr[k-1]

n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
print(kthSmallest(arr, 0, n-1, k))