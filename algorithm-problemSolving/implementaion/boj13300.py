n, k = map(int, input().split())
st = [[0, 0] for _ in range(6)]
r = 0

for _ in range(n):
  s, y = map(int, input().split())
  st[y-1][s] += 1

for _ in st:
  r += i[0] // k + (1 if i[0] % k else 0) + i[1] // k + (1 if i[1] % k else 0)
  
 print(r)
