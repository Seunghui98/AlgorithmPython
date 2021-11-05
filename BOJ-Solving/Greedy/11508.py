# 2+1세일 - BOJ 11508 
# 그리디 알고리즘
import sys

input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    x = int(input())
    data.append(x)

data.sort(reverse=True)
cost = 0
for i in range(n):
    if (i%3!=2):
        cost += data[i]

print(cost)
