#Geek wants to make a special space for candies on his bookshelf. Currently, it has N books, each of whose height is represented by the array height[] and has unit width.
#Help him select 2 books such that he can store maximum candies between them by removing all the other books from between the selected books. 
#The task is to find out the area between two books that can hold the maximum candies without changing the original position of selected books. 

class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
           maxcandy = 0
           i = 0 
           j = len(height) - 1
           
           while i < j:
               maxcandy = max(maxcandy, min(height[i],height[j]) * (j-i-1) )
               if height[i] > height[j]:
                   j -= 1
               else:
                   i += 1
           return maxcandy
