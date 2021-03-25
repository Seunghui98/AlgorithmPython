# SW 역량 테스트 - 이코테 p.349
import sys
from itertools import permutations


input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
operate = list(map(int, input().split()))
op = ['+', '-', '*', '//']
oper = []

for i in range(4):
    for _ in range((operate[i])):
        oper.append(op[i])


result = list(permutations(oper, n-1))
INF = int(1e9)
max_value = -INF
min_value = INF


for i in range(len(result)):
    what = data[0]
    for k in range(1, n):
        if result[i][k-1] == '+':
            what += data[k]
        elif result[i][k-1] == '-':
            what -= data[k]
        elif result[i][k-1] == '*':
            what *= data[k]
        else:
            if what < 0:
                what = -((-what)//data[k])
            else:
                what //= data[k]
    max_value = max(max_value, what)
    min_value = min(min_value, what)


print(max_value)
print(min_value)



