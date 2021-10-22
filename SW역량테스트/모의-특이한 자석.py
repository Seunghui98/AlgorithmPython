# SWEA - 특이한 자석
# 구현 + 재귀
from collections import deque
T = int(input())

def move_left(n, d):
    if (n-1) < 0:
        return
    if chain[n][6] != chain[n-1][2]:
        move_left(n-1, -d)
        chain[n-1].rotate(-d)


def move_right(n, d):
    if (n+1) > 3:
        return
    if chain[n][2] != chain[n+1][6]:
        move_right(n+1, -d)
        chain[n+1].rotate(-d)


for test_case in range(1, T+1):
    k = int(input())
    chain = [deque(list(map(int, input().split()))) for _ in range(4)]

    for _ in range(k):
        n, d = map(int, input().split())
        n -= 1
        move_left(n, d)
        move_right(n, d)
        chain[n].rotate(d)

    cnt = 0
    for i in range(4):
        if chain[i][0] == 1:
            cnt += (2**i)

    print(f'#{test_case} {cnt}')
