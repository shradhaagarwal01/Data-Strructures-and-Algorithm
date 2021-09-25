#Python can store large values in int

def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans
    
    
    
    
tc = int(input())
while tc > 0:
    n = int(input())
    ans = fact(n)
    print(ans)
    tc -= 1
