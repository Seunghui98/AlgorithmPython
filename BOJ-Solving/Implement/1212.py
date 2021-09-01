# 8진수 2진수 - BOJ 1212
# 8진수 -> 10진수 -> 2진수
import sys

input = sys.stdin.readline

n = input()

n = int(n, 8)
n = format(n, 'b')
print(n)



