#BOJ 통계학 2108.py
from collections import Counter
n= int(input())
data = []

for _ in range(n):
  data.append(int(input()))

data.sort()

v = 0
if n == 1:
  v = data[0]
else:
  c = Counter(data).most_common(2)
  if c[0][1] == c[1][1]:
    v = c[1][0]
  else:
    v = c[0][0]
    


print(round(sum(data) / len(data)))
print(data[(n-1)//2])
print(v)
print(max(data)-min(data))
