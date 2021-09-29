#In the game of Restricted Pacman, an infinite linear path is given. 
#Pacman has to start at position 0 and eat as many candies as possible.
#In one move he can only jump a distance of either M or N.  
#If M and N are coprime numbers, find how many candies will be left on the board after the game is over.
#Note: The result is always finite as after a point X every index in the infinite path can be visited. 


def candies(m,n): 
    return ((m-1)*(n-1))//2
