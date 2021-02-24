# BOJ 좌표 정렬하기2 11651번
n = int(input())
data = []
for _ in range(n):
  x, y = map(int, input().split())
  data.append([x,y])

data.sort(key= lambda x: (x[1], x[0]))

for i in data:
  print(i[0], i[1])
