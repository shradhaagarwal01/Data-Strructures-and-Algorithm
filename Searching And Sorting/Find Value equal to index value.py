class Solution:

    def valueEqualToIndex(self,arr, n):
        # code here
        arr1 = []
        for i in range(n):
            if arr[i]==i+1:
                arr1.append(i+1)
        return arr1



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends
