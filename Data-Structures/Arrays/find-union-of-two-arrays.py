def union(arr1,arr2):
    count = len(set(arr1+arr2))
    return count

n,m = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
print(union(arr1,arr2))