# 컨베이어 벨트 위의 로봇 - BOJ 20055
# 구현
from collections import deque

n, k = map(int, input().split())
q = deque()
lst = list(map(int, input().split()))
q.extend(lst)
answer = 0

robot = deque([0]*(n*2))

while True:
    q.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    for i in range(n-2, -1, -1):
        if (robot[i] != 0 and robot[i+1] == 0 and q[i+1] >= 1):
            q[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = robot[0]
    robot[n-1] = 0

    if q[0] >= 1:
        q[0] -= 1
        robot[0] = 1
    answer += 1
    if q.count(0) >= k:
        break


print(answer)
