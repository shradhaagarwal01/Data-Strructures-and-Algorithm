def getMinDiff(arr, n, k):
        # code here
        arr = sorted(arr)
        mini = arr[0]
        maxi = arr[n-1]
        ans = maxi-mini
        for i in range(len(arr)):
            if(arr[i]>=k):
                mn = min(arr[i]-k,mini+k)
                mx = max(arr[i-1]+k,maxi-k)
                ans = min(ans,mx-mn)
        return ans