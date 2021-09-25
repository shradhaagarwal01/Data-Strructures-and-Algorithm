def countOccurence(arr,n,k):
    d = {}
    for i in arr:
        d[i] = d.get(i,0)+1
    count = 0
    for i in d:
        if d[i] > n/k:
            count = count+1
    
    return count
