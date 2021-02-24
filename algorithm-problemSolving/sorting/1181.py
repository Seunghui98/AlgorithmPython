# BOJ 단어 정렬 1181번
n = int(input())
data = []

for _ in range(n):
  n = str(input())
  data.append((n, len(n)))
    
# 중복제거    
data = list(set(data))
data.sort(key = lambda x:(x[1], x[0]))

for i in data:
  print(i[0])
