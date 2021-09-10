# 소가 길을 건너간 이유1 - BOJ 14467
# 단순구현
import sys

input = sys.stdin.readline


n = int(input())
cow_dict = {}
cnt = 0

for i in range(n):
    cow, dir = map(int, input().split())
    if cow not in cow_dict.keys():
        cow_dict[cow] = dir
    else:
        if cow_dict[cow] == dir:
            continue
        else:
            cnt += 1
            cow_dict[cow] = dir

print(cnt)
