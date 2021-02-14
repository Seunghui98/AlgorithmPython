n, k = map(int, input().split())

t=0 
r=0 
while n>=k: 
    t=n//k 
    r+=k*t 
    n=n%k+t 

r+=n 
print(r)
