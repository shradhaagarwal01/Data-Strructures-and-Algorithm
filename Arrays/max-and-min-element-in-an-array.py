def getMinMax(low, high, arr):
    arr_min = min(arr)
    arr_max = max(arr)
    return arr_max,arr_min
	


arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)
