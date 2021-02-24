#BOJ 수 정렬하기2 2751
n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))

for i in sorted(data):
  print(i)
