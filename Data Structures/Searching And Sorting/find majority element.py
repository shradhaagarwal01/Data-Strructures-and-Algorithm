def majorityElement(arr,N):
    d = {}
    for i in arr:
        d[i] = d.get(i,0)+1
    for i in arr:
        if d[i]>N//2:
            return i
    return -1
