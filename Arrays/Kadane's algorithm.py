def maxSubArraySum(arr,n):
    ##Your code here
    max = 0
    end = 0
    for i in range(n):
        end = end+arr[i]
        if end<0:
            end = 0
        elif max<end:
            max = end
    return max
    


import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
