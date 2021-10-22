# SWEA - 활주로건설
# 구현
T = int(input())
def check(b, n, x):
    visited= [False for _ in range(n)]
    for i in range(0, n-1):
        if b[i] == b[i+1]:
            continue
        elif abs(b[i]-b[i+1]) > 1:
            return False
        elif b[i] > b[i+1]:
            temp = b[i+1]
            for j in range(i+1, i+x+1):
                if 0 <= j < n:
                    if temp != b[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        else:
            temp = b[i]
            for j in range(i, i-x, -1):
                if 0 <= j < n:
                    if temp != b[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

for test_case in range(T):
    n, x = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        if check(board[i], n, x):
            cnt += 1

    board = list(map(list, zip(*board[::-1])))
    for i in range(n):
        if check(board[i], n, x):
            cnt += 1

    print(f'#{test_case+1} {cnt}')
