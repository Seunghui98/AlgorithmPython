# 최대공약수 - BOJ 2824
# 최대공약수
import sys
from math import gcd

input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_num = 1
b_num = 1

for i in range(n):
    a_num *= a[i]

for i in range(m):
    b_num *= b[i]

answer = gcd(a_num, b_num)
answer = str(answer)

if len(answer) > 9:
    print(answer[len(answer)-9:])
else:
    print(answer)
