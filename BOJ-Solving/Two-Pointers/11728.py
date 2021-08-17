# 배열합치기 - BOJ 11728
# 투포인터 - 배열합치기
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
list_C = [0] * (n+m)

i = 0
j = 0
k = 0

while i < n or j < m:
    if j >= m or (i < n and list_A[i] <= list_B[j]):
        list_C[k] = list_A[i]
        i += 1
    else:
        list_C[k] = list_B[j]
        j += 1
    k +=1

for c in list_C:
    print(c, end=' ')
