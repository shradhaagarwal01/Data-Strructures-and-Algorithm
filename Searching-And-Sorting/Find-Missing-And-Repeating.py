def findTwoElement(arr, n): 
        # code here
        d = {}
        ans = [-1,-1]
        for i in arr:
            if i not in d:
                d[i] = True
            else:
                ans[0] = i

        for i in range(1,len(arr)+1):
            if i not in d:
                ans[1] = i
                
        return ans
