#최소, 최대 2 - BOJ 20053
# 간단 구현
import sys


input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    print(min(data), max(data))


