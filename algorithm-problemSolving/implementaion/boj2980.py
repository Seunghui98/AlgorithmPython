n, l = map(int, input().split())
t = 0
pre = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    
    t += d - pre
    pre = d
    
    cycle = t % (r+g)
    if cycle <= r:
        t += r - cycle

print(t + (l - pre))
