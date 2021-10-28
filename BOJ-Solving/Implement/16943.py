# 숫자 재배치 - BOJ 16943
# 구현(순열)
from itertools import permutations

a, b = map(int, input().split())

data = []
for i in str(a):
    data.append(i)

num = []
for p in permutations(data, len(data)):
    num.append(''.join(list(p)))

num.sort(reverse=True)


for n in range(len(num)):
    if int(num[n]) < b and num[n][0] != '0':
        print(num[n])
        break
    if n == len(num)-1:
        print(-1)
        break
