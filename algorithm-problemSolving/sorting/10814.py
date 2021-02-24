# BOJ 나이순 정렬 10814번
n = int(input())
data = []

for i in range(n):
  age, name = input().split()
  data.append([int(age), name, i])

data.sort(key= lambda x:(x[0], x[2]))

for i in data:
  print(i[0], i[1])

