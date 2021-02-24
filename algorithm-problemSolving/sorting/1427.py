# BOJ 소트인사이드 1427 번
data = list(map(int, input()))

data.sort(reverse=True)

for i in data:
  print(i, end='')
