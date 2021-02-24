#BOJ 수 정렬하기 2750번
n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))

data.sort()
for i in data:
  print(i)
