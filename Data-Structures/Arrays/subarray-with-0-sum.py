#Hashing is Used
def subArrayExists(arr,n):
    d = {}
    sum = 0
    for i in range(len(arr)):
        sum = sum+arr[i]
        if sum==0 or sum in d:
            return True
        d[sum] = d.get(sum)
    return False