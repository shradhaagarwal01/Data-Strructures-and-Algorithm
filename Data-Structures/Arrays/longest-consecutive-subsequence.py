def findLongestConseqSubseq(arr, N):
    #code here
    d = {}
    for i in arr:
        d[i] = d.get(i,0)+1
    ans = 0
    for i in arr:
        if i-1 not in d:
            q = i
            while q in d:
                    q = q+1
            ans = max(ans,q-i)
    
    return ans