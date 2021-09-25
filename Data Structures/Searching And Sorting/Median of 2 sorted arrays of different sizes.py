#Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.
import sys
class Solution():
    def MedianOfArrays(self,array1, array2):
        new_array = array1.copy()
        new_array.extend(array2)
        new_array = sorted(list(new_array))
        length = len(new_array)
        if length % 2 != 0:  # odd
            median_index = int((length+1) / 2)-1
            median_element = new_array[median_index]
            return median_element
        else:
            median_index_1 = int(length/2)-1
            median_index_2 = median_index_1 + 1
            median_element_1 = new_array[median_index_1]
            median_element_2 = new_array[median_index_2]
            result = (median_element_2 + median_element_1) / 2
            if result - int(result) != 0:
                return result
            else:
                return int(result)
