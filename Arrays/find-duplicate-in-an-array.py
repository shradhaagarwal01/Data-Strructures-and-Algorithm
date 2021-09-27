def findDuplicate(arr):
    d = set()
    for i in arr:
        if i in d:
            return i
        d.add(i)
    


n=int(input())
arr=[int(x) for x in input().strip().split()]
print(findDuplicate(arr))
