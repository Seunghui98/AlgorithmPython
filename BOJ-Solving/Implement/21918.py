# 전구 - BOJ 21918
# 단순 구현
import sys


input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        array[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if array[i] == 1:
                array[i] = 0
            else:
                array[i] = 1
    elif a == 3:
        for i in range(b-1, c):
            array[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            array[i] = 1

for i in array:
    print(i, end=' ')
