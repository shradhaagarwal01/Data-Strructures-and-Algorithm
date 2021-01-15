#valley-peak approach 
'''  
                      80 
                      / 
       30            / 
      /  \          25 
     /    15       / 
    /      \      / 
   2        10   / 
              \ / 
               8 
'''           
def maxProfit(price, n): 
  result = 0
  for i in range(1, n): 
      sub = price[i]-price[i-1]
      if sub>0:
        result = result+sub
  return result 


# Driver function 
price = [2, 30, 15, 10, 8, 25, 80]
print "Maximum profit is", maxProfit(price, len(price)) 
